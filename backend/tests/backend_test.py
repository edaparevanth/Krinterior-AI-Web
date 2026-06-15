"""KRINTERIOR AI – Backend integration tests (pytest)."""
import base64
import os
import uuid

import pytest
import requests

BASE_URL = os.environ.get("REACT_APP_BACKEND_URL")
if not BASE_URL:
    # Try frontend .env if env var not set
    try:
        with open("/app/frontend/.env") as f:
            for line in f:
                if line.startswith("REACT_APP_BACKEND_URL="):
                    BASE_URL = line.split("=", 1)[1].strip().strip('"')
                    break
    except Exception:
        pass

assert BASE_URL, "REACT_APP_BACKEND_URL must be configured"
BASE_URL = BASE_URL.rstrip("/")
API = f"{BASE_URL}/api"

# 1x1 transparent PNG
TINY_PNG_B64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
)

EXISTING_EMAIL = "test.user.krinterior@example.com"
EXISTING_PASSWORD = "Test@123456"


# ---------- fixtures ----------
@pytest.fixture(scope="session")
def http():
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json"})
    return s


@pytest.fixture(scope="session")
def auth_token(http):
    """Login existing seeded account; if missing, sign it up."""
    r = http.post(
        f"{API}/auth/login",
        json={"email": EXISTING_EMAIL, "password": EXISTING_PASSWORD},
        timeout=30,
    )
    if r.status_code == 200:
        return r.json()["access_token"]
    # signup
    r2 = http.post(
        f"{API}/auth/signup",
        json={
            "email": EXISTING_EMAIL,
            "password": EXISTING_PASSWORD,
            "full_name": "Test User",
        },
        timeout=30,
    )
    if r2.status_code == 200:
        return r2.json()["access_token"]
    pytest.skip(f"Cannot authenticate test user: {r2.status_code} {r2.text}")


@pytest.fixture(scope="session")
def auth_headers(auth_token):
    return {"Authorization": f"Bearer {auth_token}", "Content-Type": "application/json"}


# ---------- Root ----------
def test_root(http):
    r = http.get(f"{API}/", timeout=20)
    assert r.status_code == 200
    data = r.json()
    assert data.get("app") == "KRINTERIOR AI"
    assert data.get("status") == "ok"


# ---------- Auth: signup / login / me ----------
class TestAuth:
    def test_signup_new_user_returns_token_and_user(self, http):
        email = f"test_signup_{uuid.uuid4().hex[:8]}@example.com"
        r = http.post(
            f"{API}/auth/signup",
            json={"email": email, "password": "Test@123456", "full_name": "Foo Bar"},
            timeout=30,
        )
        assert r.status_code == 200, r.text
        data = r.json()
        assert "access_token" in data and isinstance(data["access_token"], str)
        assert data["token_type"] == "bearer"
        assert data["user"]["email"] == email
        assert data["user"]["full_name"] == "Foo Bar"
        assert "id" in data["user"]

    def test_signup_duplicate_email_fails(self, http):
        r = http.post(
            f"{API}/auth/signup",
            json={"email": EXISTING_EMAIL, "password": EXISTING_PASSWORD},
            timeout=30,
        )
        # may be 400 (already registered)
        assert r.status_code == 400
        assert "already" in r.json()["detail"].lower()

    def test_login_success(self, http):
        r = http.post(
            f"{API}/auth/login",
            json={"email": EXISTING_EMAIL, "password": EXISTING_PASSWORD},
            timeout=30,
        )
        assert r.status_code == 200, r.text
        data = r.json()
        assert isinstance(data["access_token"], str)
        assert data["user"]["email"] == EXISTING_EMAIL

    def test_login_wrong_password(self, http):
        r = http.post(
            f"{API}/auth/login",
            json={"email": EXISTING_EMAIL, "password": "wrong-pass"},
            timeout=30,
        )
        assert r.status_code == 401

    def test_me_requires_auth(self, http):
        r = http.get(f"{API}/auth/me", timeout=20)
        assert r.status_code == 401

    def test_me_with_bearer(self, http, auth_headers):
        r = http.get(f"{API}/auth/me", headers=auth_headers, timeout=20)
        assert r.status_code == 200
        data = r.json()
        assert data["email"] == EXISTING_EMAIL
        assert "id" in data

    def test_google_session_bogus(self, http):
        r = http.post(
            f"{API}/auth/google/session",
            json={"session_id": "totally-bogus-session-id"},
            timeout=30,
        )
        assert r.status_code == 401


# ---------- Auth enforcement on other endpoints ----------
class TestAuthEnforcement:
    def test_projects_list_requires_auth(self, http):
        assert http.get(f"{API}/projects", timeout=20).status_code == 401

    def test_design_generate_requires_auth(self, http):
        r = http.post(
            f"{API}/design/generate",
            json={
                "image_base64": TINY_PNG_B64,
                "room_type": "Living Room",
                "budget": 200000,
                "color_palette": "Warm Beige",
            },
            timeout=20,
        )
        assert r.status_code == 401

    def test_vastu_requires_auth(self, http):
        r = http.post(
            f"{API}/vastu/analyze", json={"project_id": "anything"}, timeout=20
        )
        assert r.status_code == 401


# ---------- Design generation (LLM heavy; runs after auth tests) ----------
class TestDesignAndProjects:
    """Full E2E: generate -> save -> list -> get -> patch -> vastu re-analyze -> delete."""

    created_project_id: str | None = None
    generated_payload: dict | None = None

    def test_01_generate_design(self, http, auth_headers):
        body = {
            "image_base64": TINY_PNG_B64,
            "room_type": "Living Room",
            "budget": 200000,
            "color_palette": "Warm Beige",
            "requirements": "Modern Indian look with plants",
        }
        r = http.post(
            f"{API}/design/generate",
            json=body,
            headers=auth_headers,
            timeout=180,  # Gemini Nano Banana may take 20-50s + JSON calls
        )
        assert r.status_code == 200, f"{r.status_code} {r.text[:500]}"
        data = r.json()
        # generated_image
        gen = data.get("generated_image")
        assert isinstance(gen, str) and len(gen) > 100
        # base64 decodable
        try:
            base64.b64decode(gen[:200] + "==")
        except Exception:
            pytest.fail("generated_image not base64")
        # furniture_estimate
        items = data.get("furniture_estimate")
        assert isinstance(items, list) and len(items) >= 1
        for it in items:
            assert "name" in it and ("price_inr" in it or "price" in it)
        # total_cost
        assert isinstance(data.get("total_cost"), int)
        assert data["total_cost"] > 0
        # space_analysis
        assert isinstance(data.get("space_analysis"), dict)
        # vastu
        assert isinstance(data.get("vastu_report"), dict)
        score = data.get("vastu_score")
        assert isinstance(score, int) and 60 <= score <= 98
        # stash for next tests
        TestDesignAndProjects.generated_payload = {
            "name": f"TEST_proj_{uuid.uuid4().hex[:6]}",
            "original_image": TINY_PNG_B64,
            "generated_image": gen,
            "room_type": body["room_type"],
            "budget": body["budget"],
            "color_palette": body["color_palette"],
            "requirements": body["requirements"],
            "furniture_estimate": items,
            "total_cost": data["total_cost"],
            "vastu_score": score,
            "vastu_report": data["vastu_report"],
            "space_analysis": data["space_analysis"],
        }

    def test_02_create_project(self, http, auth_headers):
        payload = TestDesignAndProjects.generated_payload
        assert payload, "Generation must succeed first"
        r = http.post(f"{API}/projects", json=payload, headers=auth_headers, timeout=30)
        assert r.status_code == 200, r.text
        data = r.json()
        assert data["id"] and isinstance(data["id"], str)
        assert data["name"] == payload["name"]
        assert data["room_type"] == payload["room_type"]
        assert data["total_cost"] == payload["total_cost"]
        # No mongo _id leak
        assert "_id" not in data
        TestDesignAndProjects.created_project_id = data["id"]

    def test_03_list_projects_excludes_heavy_fields(self, http, auth_headers):
        r = http.get(f"{API}/projects", headers=auth_headers, timeout=20)
        assert r.status_code == 200
        rows = r.json()
        assert isinstance(rows, list) and len(rows) >= 1
        ids = [p["id"] for p in rows]
        assert TestDesignAndProjects.created_project_id in ids
        sample = next(p for p in rows if p["id"] == TestDesignAndProjects.created_project_id)
        # Heavy fields excluded
        for f in (
            "original_image",
            "generated_image",
            "furniture_estimate",
            "vastu_report",
            "space_analysis",
        ):
            assert f not in sample, f"Field {f} should be excluded from list view"
        # Light fields present
        assert sample["name"]
        assert "_id" not in sample

    def test_04_get_project_full(self, http, auth_headers):
        pid = TestDesignAndProjects.created_project_id
        r = http.get(f"{API}/projects/{pid}", headers=auth_headers, timeout=20)
        assert r.status_code == 200
        data = r.json()
        assert data["id"] == pid
        assert isinstance(data.get("generated_image"), str) and len(data["generated_image"]) > 50
        assert isinstance(data.get("furniture_estimate"), list)
        assert isinstance(data.get("vastu_report"), dict)
        assert "_id" not in data

    def test_05_get_project_404(self, http, auth_headers):
        r = http.get(
            f"{API}/projects/non-existent-id", headers=auth_headers, timeout=20
        )
        assert r.status_code == 404

    def test_06_rename_project(self, http, auth_headers):
        pid = TestDesignAndProjects.created_project_id
        new_name = f"TEST_renamed_{uuid.uuid4().hex[:6]}"
        r = http.patch(
            f"{API}/projects/{pid}",
            json={"name": new_name},
            headers=auth_headers,
            timeout=20,
        )
        assert r.status_code == 200
        assert r.json()["name"] == new_name
        # verify persistence
        g = http.get(f"{API}/projects/{pid}", headers=auth_headers, timeout=20)
        assert g.json()["name"] == new_name

    def test_07_vastu_reanalyze(self, http, auth_headers):
        pid = TestDesignAndProjects.created_project_id
        r = http.post(
            f"{API}/vastu/analyze",
            json={"project_id": pid},
            headers=auth_headers,
            timeout=90,
        )
        assert r.status_code == 200, r.text
        data = r.json()
        score = data.get("vastu_score")
        assert isinstance(score, int) and 60 <= score <= 98
        assert isinstance(data.get("vastu_report"), dict)
        # Verify persistence
        g = http.get(f"{API}/projects/{pid}", headers=auth_headers, timeout=20)
        assert g.status_code == 200
        assert g.json()["vastu_score"] == score

    def test_08_vastu_analyze_404(self, http, auth_headers):
        r = http.post(
            f"{API}/vastu/analyze",
            json={"project_id": "non-existent"},
            headers=auth_headers,
            timeout=30,
        )
        assert r.status_code == 404

    def test_09_delete_project(self, http, auth_headers):
        pid = TestDesignAndProjects.created_project_id
        r = http.delete(f"{API}/projects/{pid}", headers=auth_headers, timeout=20)
        assert r.status_code == 200
        # Verify gone
        g = http.get(f"{API}/projects/{pid}", headers=auth_headers, timeout=20)
        assert g.status_code == 404

    def test_10_delete_project_404(self, http, auth_headers):
        r = http.delete(
            f"{API}/projects/non-existent", headers=auth_headers, timeout=20
        )
        assert r.status_code == 404
