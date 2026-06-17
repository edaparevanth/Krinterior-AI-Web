"""KRINTERIOR AI – Smart Interior Studio backend."""
import base64
import json
import logging
import os
import re
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional

import httpx
import jwt
from dotenv import load_dotenv
from fastapi import APIRouter, Cookie, Depends, FastAPI, Header, HTTPException, Request, Response, status
from motor.motor_asyncio import AsyncIOMotorClient
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr, Field
from starlette.middleware.cors import CORSMiddleware

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / ".env")

MONGO_URL = os.environ["MONGO_URL"]
DB_NAME = os.environ["DB_NAME"]
EMERGENT_LLM_KEY = os.environ["EMERGENT_LLM_KEY"]
JWT_SECRET = os.environ["JWT_SECRET"]
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM", "HS256")
JWT_EXPIRE_MINUTES = int(os.environ.get("JWT_EXPIRE_MINUTES", "10080"))

GEMINI_IMAGE_MODEL = "gemini-3.1-flash-image-preview"
GEMINI_TEXT_MODEL = "gemini-2.5-flash"

# Emergent universal LLM proxy – OpenAI-compatible Chat Completions endpoint.
# Same shape as `https://api.openai.com/v1/chat/completions` plus a non-standard
# `message.images` field on responses for Gemini image-generation models.
EMERGENT_LLM_BASE_URL = os.environ.get(
    "EMERGENT_LLM_BASE_URL", "https://integrations.emergentagent.com/llm"
)

EMERGENT_AUTH_URL = "https://demobackend.emergentagent.com/auth/v1/env/oauth/session-data"

client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]
users_col = db["users"]
projects_col = db["projects"]
sessions_col = db["user_sessions"]
jobs_col = db["design_jobs"]

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("krinterior")

app = FastAPI(title="KRINTERIOR AI")
api = APIRouter(prefix="/api")


# ---------- helpers ----------
def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def create_token(user_id: str) -> str:
    payload = {
        "sub": user_id,
        "exp": now_utc() + timedelta(minutes=JWT_EXPIRE_MINUTES),
        "iat": now_utc(),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


async def _resolve_user_from_token(token: str) -> Optional[dict]:
    """Try Google session token first, then JWT."""
    if not token:
        return None
    # 1) Google session token in DB
    session = await sessions_col.find_one({"session_token": token}, {"_id": 0})
    if session:
        expires_at = session.get("expires_at")
        if isinstance(expires_at, str):
            expires_at = datetime.fromisoformat(expires_at)
        if expires_at and expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo=timezone.utc)
        if expires_at and expires_at < now_utc():
            return None
        user = await users_col.find_one(
            {"id": session["user_id"]}, {"_id": 0, "password_hash": 0}
        )
        return user
    # 2) JWT
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user_id = payload.get("sub")
    except jwt.PyJWTError:
        return None
    user = await users_col.find_one({"id": user_id}, {"_id": 0, "password_hash": 0})
    return user


async def get_current_user(
    request: Request,
    authorization: Optional[str] = Header(None),
    session_token: Optional[str] = Cookie(None),
) -> dict:
    """Accept either Bearer token (JWT or Google session token) or cookie."""
    token = None
    if authorization and authorization.lower().startswith("bearer "):
        token = authorization.split(" ", 1)[1].strip()
    if not token and session_token:
        token = session_token
    user = await _resolve_user_from_token(token) if token else None
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user


# ---------- models ----------
class SignupIn(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=128)
    full_name: Optional[str] = None


class LoginIn(BaseModel):
    email: EmailStr
    password: str


class AuthOut(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: dict


class UpdateProfileIn(BaseModel):
    full_name: Optional[str] = None


class GenerateDesignIn(BaseModel):
    image_base64: str
    room_type: str
    budget: int
    color_palette: str
    requirements: Optional[str] = ""


class AnalyzeDesignIn(BaseModel):
    room_type: str
    budget: int
    color_palette: str
    requirements: Optional[str] = ""


class SaveProjectIn(BaseModel):
    name: str
    original_image: str
    generated_image: str
    room_type: str
    budget: int
    color_palette: str
    requirements: Optional[str] = ""
    furniture_estimate: list
    total_cost: int
    vastu_score: int
    vastu_report: dict
    space_analysis: dict


class RenameProjectIn(BaseModel):
    name: str


class GoogleAuthIn(BaseModel):
    session_id: str


# ---------- email/password auth ----------
def _public_user(user: dict) -> dict:
    return {
        "id": user["id"],
        "email": user.get("email"),
        "full_name": user.get("full_name") or user.get("name"),
        "name": user.get("full_name") or user.get("name"),
        "picture": user.get("picture"),
        "created_at": user.get("created_at"),
    }


@api.post("/auth/signup", response_model=AuthOut)
async def signup(body: SignupIn):
    email = body.email.lower()
    existing = await users_col.find_one({"email": email})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user_id = str(uuid.uuid4())
    doc = {
        "id": user_id,
        "email": email,
        "full_name": body.full_name or email.split("@")[0],
        "password_hash": pwd_context.hash(body.password),
        "created_at": now_utc().isoformat(),
        "auth_provider": "email",
    }
    await users_col.insert_one(doc)
    return AuthOut(access_token=create_token(user_id), user=_public_user(doc))


@api.post("/auth/login", response_model=AuthOut)
async def login(body: LoginIn):
    email = body.email.lower()
    user = await users_col.find_one({"email": email})
    if not user or not user.get("password_hash") or not pwd_context.verify(
        body.password, user["password_hash"]
    ):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return AuthOut(access_token=create_token(user["id"]), user=_public_user(user))


@api.post("/auth/google/session")
async def google_session(body: GoogleAuthIn, response: Response):
    """Exchange Emergent Google session_id for a backend session_token cookie."""
    async with httpx.AsyncClient(timeout=15) as http:
        r = await http.get(
            EMERGENT_AUTH_URL,
            headers={"X-Session-ID": body.session_id},
        )
    if r.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid Google session")
    data = r.json()
    email = (data.get("email") or "").lower()
    if not email:
        raise HTTPException(status_code=400, detail="Email missing from Google")

    user = await users_col.find_one({"email": email})
    if not user:
        user_id = str(uuid.uuid4())
        user = {
            "id": user_id,
            "email": email,
            "full_name": data.get("name") or email.split("@")[0],
            "picture": data.get("picture"),
            "created_at": now_utc().isoformat(),
            "auth_provider": "google",
        }
        await users_col.insert_one(user)
    else:
        await users_col.update_one(
            {"id": user["id"]},
            {"$set": {"picture": data.get("picture"), "full_name": data.get("name") or user.get("full_name")}},
        )

    session_token = data.get("session_token") or str(uuid.uuid4())
    expires_at = now_utc() + timedelta(days=7)
    await sessions_col.update_one(
        {"session_token": session_token},
        {
            "$set": {
                "session_token": session_token,
                "user_id": user["id"],
                "expires_at": expires_at,
                "created_at": now_utc(),
            }
        },
        upsert=True,
    )

    response.set_cookie(
        key="session_token",
        value=session_token,
        max_age=7 * 24 * 60 * 60,
        httponly=True,
        secure=True,
        samesite="none",
        path="/",
    )
    return {"access_token": session_token, "token_type": "bearer", "user": _public_user(user)}


@api.post("/auth/logout")
async def logout(response: Response, authorization: Optional[str] = Header(None), session_token: Optional[str] = Cookie(None)):
    token = None
    if authorization and authorization.lower().startswith("bearer "):
        token = authorization.split(" ", 1)[1].strip()
    if not token:
        token = session_token
    if token:
        await sessions_col.delete_one({"session_token": token})
    response.delete_cookie("session_token", path="/")
    return {"ok": True}


@api.get("/auth/me")
async def me(user: dict = Depends(get_current_user)):
    return _public_user(user)


@api.put("/auth/me")
async def update_me(body: UpdateProfileIn, user: dict = Depends(get_current_user)):
    update = {}
    if body.full_name is not None:
        update["full_name"] = body.full_name
    if update:
        await users_col.update_one({"id": user["id"]}, {"$set": update})
    fresh = await users_col.find_one(
        {"id": user["id"]}, {"_id": 0, "password_hash": 0}
    )
    return _public_user(fresh)


# ---------- AI helpers ----------
def _strip_data_url(b64: str) -> str:
    if b64.startswith("data:"):
        return b64.split(",", 1)[-1]
    return b64


def _extract_json(text: str) -> Optional[dict]:
    if not text:
        return None
    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if fenced:
        try:
            return json.loads(fenced.group(1))
        except json.JSONDecodeError:
            pass
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        try:
            return json.loads(text[start : end + 1])
        except json.JSONDecodeError:
            return None
    return None


async def _emergent_chat_completion(payload: dict, timeout: float = 90.0) -> dict:
    """Call the Emergent universal LLM proxy (OpenAI-compatible).
    Returns the raw JSON response dict."""
    headers = {
        "Authorization": f"Bearer {EMERGENT_LLM_KEY}",
        "Content-Type": "application/json",
    }
    async with httpx.AsyncClient(timeout=timeout) as http:
        r = await http.post(
            f"{EMERGENT_LLM_BASE_URL}/chat/completions",
            json=payload,
            headers=headers,
        )
    if r.status_code != 200:
        detail = r.text[:300]
        logger.error("Emergent LLM error %s: %s", r.status_code, detail)
        raise HTTPException(
            status_code=502, detail=f"LLM provider error ({r.status_code})"
        )
    return r.json()


async def call_gemini_image_edit(prompt: str, image_b64: str) -> str:
    """Send an empty-room image to Gemini Nano Banana and return the
    generated furnished room as base64. Uses the OpenAI multimodal format."""
    payload = {
        "model": f"gemini/{GEMINI_IMAGE_MODEL}",
        "modalities": ["image", "text"],
        "messages": [
            {
                "role": "system",
                "content": "You are KRINTERIOR AI, a world-class Indian interior designer that transforms empty rooms into photorealistic furnished interiors.",
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{image_b64}"},
                    },
                ],
            },
        ],
    }
    data = await _emergent_chat_completion(payload, timeout=120.0)
    try:
        message = data["choices"][0]["message"]
    except (KeyError, IndexError):
        raise HTTPException(status_code=502, detail="AI returned empty response")

    # Gemini image-generation responses include images in a non-standard
    # `message.images` list. Each item is {"image_url": {"url": "data:...;base64,..."}}
    for img in message.get("images") or []:
        url = (img.get("image_url") or {}).get("url", "")
        if "base64," in url:
            return url.split("base64,", 1)[1]

    raise HTTPException(
        status_code=502, detail="AI did not return any image. Please try again."
    )


async def call_gemini_text_json(
    system: str, prompt: str, fallback: Optional[dict] = None
) -> dict:
    """Call Gemini Flash through the Emergent proxy and parse a JSON response.
    Retries up to 3x, then returns `fallback` if provided, else raises 502."""
    last_text = ""
    payload_base = {
        "model": f"gemini/{GEMINI_TEXT_MODEL}",
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
    }
    for attempt in range(3):
        try:
            data = await _emergent_chat_completion(payload_base, timeout=45.0)
            last_text = (
                data.get("choices", [{}])[0].get("message", {}).get("content") or ""
            )
        except HTTPException:
            raise
        except Exception as e:
            logger.warning("Gemini text call failed (attempt %s): %s", attempt + 1, e)
            continue
        parsed = _extract_json(last_text)
        if parsed is not None:
            return parsed
        logger.warning(
            "Gemini text returned unparseable JSON (attempt %s): %r",
            attempt + 1,
            last_text[:200],
        )
    logger.error("AI malformed response after retries: %r", last_text[:500])
    if fallback is not None:
        return fallback
    raise HTTPException(status_code=502, detail="AI returned malformed response")


def _fallback_estimate(budget: int, room_type: str) -> dict:
    items = [
        {"name": f"{room_type} sofa / centerpiece", "category": "seating", "price_inr": int(budget * 0.35)},
        {"name": "Coffee / side table set", "category": "table", "price_inr": int(budget * 0.10)},
        {"name": "Storage / TV unit", "category": "storage", "price_inr": int(budget * 0.18)},
        {"name": "Area rug", "category": "rug", "price_inr": int(budget * 0.07)},
        {"name": "Curtains & sheers", "category": "soft furnishing", "price_inr": int(budget * 0.06)},
        {"name": "Lighting (floor + table)", "category": "lighting", "price_inr": int(budget * 0.10)},
        {"name": "Wall art & mirrors", "category": "decor", "price_inr": int(budget * 0.08)},
        {"name": "Plants & accents", "category": "decor", "price_inr": int(budget * 0.06)},
    ]
    total = sum(i["price_inr"] for i in items)
    return {"items": items, "total_inr": total, "currency": "INR"}


def _fallback_space(room_type: str) -> dict:
    return {
        "estimated_size_sqft": 180,
        "available_zones": ["Main seating", "Storage wall", "Accent corner"],
        "design_opportunities": ["Layered lighting", "Indo-modern textiles", "Statement art wall"],
        "optimization_suggestions": ["Float furniture slightly off walls", "Add greenery for depth", "Use a large rug to anchor"],
    }


def _fallback_vastu(room_type: str, palette: str) -> dict:
    return {
        "score": 82,
        "summary": f"Balanced {room_type.lower()} aligned with Vastu principles.",
        "positive_aspects": [
            "Open flow of natural light",
            "Earthy palette supports grounding energy",
            "Heavy furniture positioned in south/west direction",
        ],
        "issues": [
            "Verify entry from the north or east for prosperity",
            "Avoid sharp corners aimed at seating",
        ],
        "recommendations": [
            "Place a brass/copper accent in the north-east",
            "Add a plant in the east for fresh energy",
            "Use warm lighting in the south-east",
        ],
        "energy_flow": f"The {palette.lower()} palette supports stable, calming chi flow.",
    }


# ---------- design generation ----------
DESIGN_PROMPT_TEMPLATE = """Transform this empty room photograph into a fully furnished, photorealistic INDIAN-STYLE {room_type}.

CRITICAL RULES (must preserve from original):
- Exact same walls, windows, doors, ceiling, floor
- Same camera angle, perspective, lighting direction, shadows
- Same room geometry and dimensions
- No floating or distorted furniture, no warped walls

DESIGN GUIDELINES:
- Budget: ₹{budget:,} (Indian Rupees) – choose furniture quality and quantity accordingly
- Color palette: {color_palette}
- Style: Premium modern Indian luxury, teak/walnut wood finishes, urban Indian apartment vibe
- Add appropriate furniture for a {room_type} (sofa, tables, storage, rugs, plants, art, lighting, curtains as relevant)

USER REQUIREMENTS: {requirements}

Output ONLY the finished room image, hyper-realistic, like a high-end interior magazine photo."""


@api.post("/design/generate")
async def generate_design(
    body: GenerateDesignIn, user: dict = Depends(get_current_user)
):
    """Start an async image-generation job. Returns job_id immediately so the
    frontend can poll /design/status/{job_id} and avoid the 30s edge timeout."""
    import asyncio as _asyncio

    image_b64 = _strip_data_url(body.image_base64)
    if not image_b64:
        raise HTTPException(status_code=400, detail="Missing image")

    job_id = str(uuid.uuid4())
    await jobs_col.insert_one({
        "id": job_id,
        "user_id": user["id"],
        "status": "pending",
        "created_at": now_utc().isoformat(),
    })

    prompt = DESIGN_PROMPT_TEMPLATE.format(
        room_type=body.room_type,
        budget=body.budget,
        color_palette=body.color_palette,
        requirements=body.requirements or "Premium Indian family-friendly layout",
    )

    async def _run():
        try:
            logger.info("Job %s starting (user=%s room=%s)", job_id, user["id"], body.room_type)
            generated_b64 = await call_gemini_image_edit(prompt, image_b64)
            await jobs_col.update_one(
                {"id": job_id},
                {"$set": {"status": "done", "generated_image": generated_b64,
                          "completed_at": now_utc().isoformat()}},
            )
            logger.info("Job %s done", job_id)
        except Exception as e:
            logger.exception("Job %s failed: %s", job_id, e)
            await jobs_col.update_one(
                {"id": job_id},
                {"$set": {"status": "error", "error": str(e)[:300],
                          "completed_at": now_utc().isoformat()}},
            )

    _asyncio.create_task(_run())
    return {"job_id": job_id, "status": "pending"}


@api.get("/design/status/{job_id}")
async def design_status(job_id: str, user: dict = Depends(get_current_user)):
    job = await jobs_col.find_one(
        {"id": job_id, "user_id": user["id"]}, {"_id": 0}
    )
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


@api.post("/design/analyze")
async def analyze_design(
    body: AnalyzeDesignIn, user: dict = Depends(get_current_user)
):
    """Stage 2: Furniture estimate + space analysis + Vastu (runs the 3 calls in parallel)."""
    import asyncio as _asyncio

    estimate_task = call_gemini_text_json(
        system="You are a furniture cost estimator for Indian retail markets. Always respond with strict JSON only.",
        prompt=f"""Generate a furniture cost estimate for an Indian {body.room_type} with a budget of ₹{body.budget}, palette '{body.color_palette}', requirements: '{body.requirements}'.

Return JSON in this EXACT schema:
{{
  "items": [
    {{"name": "string", "category": "string", "price_inr": integer}}
  ],
  "total_inr": integer,
  "currency": "INR"
}}

Rules:
- Include 6-10 items realistic for the room type (sofa/bed/table/chairs/storage/lighting/rug/curtains/plants/art)
- Use real Indian market prices (Urban Ladder, Pepperfry, IKEA India range)
- total_inr must equal sum of items.price_inr
- total_inr should be within ±10% of the budget ₹{body.budget}
- Use teak/walnut/modern Indian luxury references""",
        fallback=_fallback_estimate(body.budget, body.room_type),
    )

    space_task = call_gemini_text_json(
        system="You are an interior space analyst. Return JSON only.",
        prompt=f"""Analyse a {body.room_type} for interior design. Return JSON:
{{
  "estimated_size_sqft": integer,
  "available_zones": ["string"],
  "design_opportunities": ["string"],
  "optimization_suggestions": ["string"]
}}
Be concise: 3-5 items per array.""",
        fallback=_fallback_space(body.room_type),
    )

    vastu_task = call_gemini_text_json(
        system="You are a Vastu Shastra expert applying ancient Indian architectural principles to a modern interior design. Return JSON only.",
        prompt=f"""Evaluate a {body.room_type} with palette '{body.color_palette}' and requirements '{body.requirements}' from a Vastu perspective. Return JSON:
{{
  "score": integer between 60 and 98,
  "summary": "one-line verdict",
  "positive_aspects": ["string"],
  "issues": ["string"],
  "recommendations": ["string"],
  "energy_flow": "string description"
}}
Rules: 3-5 items per array. Score should reflect overall Vastu alignment.""",
        fallback=_fallback_vastu(body.room_type, body.color_palette),
    )

    estimate, space, vastu = await _asyncio.gather(estimate_task, space_task, vastu_task)

    return {
        "furniture_estimate": estimate.get("items", []),
        "total_cost": int(estimate.get("total_inr", body.budget)),
        "space_analysis": space,
        "vastu_report": vastu,
        "vastu_score": int(vastu.get("score", 80)),
    }


# ---------- projects ----------
@api.post("/projects")
async def create_project(body: SaveProjectIn, user: dict = Depends(get_current_user)):
    pid = str(uuid.uuid4())
    doc = {
        "id": pid,
        "user_id": user["id"],
        "name": body.name,
        "original_image": _strip_data_url(body.original_image),
        "generated_image": _strip_data_url(body.generated_image),
        "room_type": body.room_type,
        "budget": body.budget,
        "color_palette": body.color_palette,
        "requirements": body.requirements,
        "furniture_estimate": body.furniture_estimate,
        "total_cost": body.total_cost,
        "vastu_score": body.vastu_score,
        "vastu_report": body.vastu_report,
        "space_analysis": body.space_analysis,
        "created_at": now_utc().isoformat(),
        "updated_at": now_utc().isoformat(),
    }
    await projects_col.insert_one(doc)
    doc.pop("_id", None)
    return doc


@api.get("/projects")
async def list_projects(user: dict = Depends(get_current_user)):
    cursor = projects_col.find(
        {"user_id": user["id"]},
        {
            "_id": 0,
            "original_image": 0,
            "generated_image": 0,
            "furniture_estimate": 0,
            "vastu_report": 0,
            "space_analysis": 0,
        },
    ).sort("created_at", -1)
    return await cursor.to_list(length=200)


@api.get("/projects/{project_id}")
async def get_project(project_id: str, user: dict = Depends(get_current_user)):
    proj = await projects_col.find_one(
        {"id": project_id, "user_id": user["id"]}, {"_id": 0}
    )
    if not proj:
        raise HTTPException(status_code=404, detail="Project not found")
    return proj


@api.patch("/projects/{project_id}")
async def rename_project(
    project_id: str,
    body: RenameProjectIn,
    user: dict = Depends(get_current_user),
):
    result = await projects_col.update_one(
        {"id": project_id, "user_id": user["id"]},
        {"$set": {"name": body.name, "updated_at": now_utc().isoformat()}},
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Project not found")
    proj = await projects_col.find_one(
        {"id": project_id, "user_id": user["id"]}, {"_id": 0}
    )
    return proj


@api.delete("/projects/{project_id}")
async def delete_project(project_id: str, user: dict = Depends(get_current_user)):
    result = await projects_col.delete_one(
        {"id": project_id, "user_id": user["id"]}
    )
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"ok": True}


# ---------- vastu standalone ----------
class VastuRequest(BaseModel):
    project_id: str


@api.post("/vastu/analyze")
async def analyze_vastu(body: VastuRequest, user: dict = Depends(get_current_user)):
    proj = await projects_col.find_one(
        {"id": body.project_id, "user_id": user["id"]}, {"_id": 0}
    )
    if not proj:
        raise HTTPException(status_code=404, detail="Project not found")
    vastu = await call_gemini_text_json(
        system="You are a Vastu Shastra expert. Return JSON only.",
        prompt=f"""Re-evaluate this saved project from a deeper Vastu perspective:
Room: {proj['room_type']}, Palette: {proj['color_palette']}, Budget: ₹{proj['budget']}, Requirements: {proj.get('requirements','')}

Return JSON:
{{
  "score": integer 60-98,
  "summary": "string",
  "positive_aspects": ["string"],
  "issues": ["string"],
  "recommendations": ["string"],
  "energy_flow": "string"
}}""",
        fallback=_fallback_vastu(proj["room_type"], proj["color_palette"]),
    )
    score = int(vastu.get("score", proj.get("vastu_score", 80)))
    await projects_col.update_one(
        {"id": body.project_id},
        {"$set": {"vastu_score": score, "vastu_report": vastu}},
    )
    return {"vastu_score": score, "vastu_report": vastu}


@api.get("/")
async def root():
    return {"app": "KRINTERIOR AI", "status": "ok"}


app.include_router(api)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await users_col.create_index("email", unique=True)
    await projects_col.create_index([("user_id", 1), ("created_at", -1)])
    await sessions_col.create_index("session_token", unique=True)
    logger.info("KRINTERIOR AI backend ready")


@app.on_event("shutdown")
async def shutdown():
    client.close()
