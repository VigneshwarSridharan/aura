# aura

AI application starter with:
- Frontend: Next.js (App Router, TypeScript)
- Backend: FastAPI (Python)

## Why FastAPI for AI backends
FastAPI is a strong choice for AI workloads because it integrates naturally with Python ML/LLM libraries, offers fast async APIs, and is simple to scale into production.

## Project structure
- `frontend/` - Next.js UI and API proxy route
- `backend/` - FastAPI service

## Quick start

### 1) Backend
```bash
cd backend
# install uv once (if needed): https://docs.astral.sh/uv/getting-started/installation/
uv sync
cp .env.example .env
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 2) Frontend
In a new terminal:
```bash
cd frontend
cp .env.local.example .env.local
npm install
npm run dev
```

Then open `http://localhost:3000`.

## Next steps
- Integrate an LLM provider in `backend/app/main.py` at `/api/v1/chat`
- Add auth and rate limiting
- Add persistence (PostgreSQL + Redis)
