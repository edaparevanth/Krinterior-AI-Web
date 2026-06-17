# KRINTERIOR AI – Product Requirements

## Overview
AI-powered interior design SaaS for Indian homes. Upload an empty room → get a
photorealistic furnished design + ₹ furniture estimate + Vastu Shastra report.

## Tech Stack
- Frontend: React (CRA + craco) + Tailwind + react-router 7 + sonner toasts
- Backend: FastAPI + MongoDB (motor)
- Auth: Emergent Google OAuth + JWT email/password (both supported)
- AI: Gemini Nano Banana (`gemini-3.1-flash-image-preview`) for image edit,
  Gemini 2.5 Flash for cost/space/vastu JSON, via Emergent LLM Key

## Pages
- `/` Landing (hero, features, CTA)
- `/login`, `/signup`
- `/dashboard` (greeting, tools, recent projects)
- `/create` (5-step wizard: upload → room → budget → palette → requirements)
- `/result` (before/after slider, furniture estimate, vastu summary, shopping)
- `/projects`, `/project/:id` (design/vastu tabs)
- `/vastu` (analyze saved projects)

## Backend Endpoints (/api)
- `POST /auth/signup`, `POST /auth/login`, `GET /auth/me`, `PUT /auth/me`,
  `POST /auth/logout`, `POST /auth/google/session`
- `POST /design/generate` (image + room + budget + palette + requirements)
- `POST /projects`, `GET /projects`, `GET /projects/:id`,
  `PATCH /projects/:id`, `DELETE /projects/:id`
- `POST /vastu/analyze`

## Mongo Collections
- `users` (id, email, full_name, password_hash?, picture?, auth_provider)
- `projects` (id, user_id, name, original_image, generated_image, room_type,
  budget, color_palette, requirements, furniture_estimate[], total_cost,
  vastu_score, vastu_report, space_analysis, created_at, updated_at)
- `user_sessions` (session_token, user_id, expires_at)

## Implemented (2026-01)
- Email/password JWT signup/login/me/update
- Emergent Google OAuth callback exchange + httpOnly cookie session
- 5-step create wizard with image upload, presets, palette swatches
- Gemini Nano Banana design generation
- Furniture estimate (₹), space analysis, Vastu (60-98 score)
- Before/After slider, save/rename/delete project, download image
- Vastu standalone page with re-analyze
- Shopping suggestions deep-linking to Indian retailers (Urban Ladder, IKEA,
  Pepperfry, Amazon India)

## Backlog (P1)
- Subscription/billing (Stripe/Razorpay)
- 3D walkthrough (WebXR / R3F)
- Admin panel
- Project sharing & PDF export

## Test Credentials
See `/app/memory/test_credentials.md`.
