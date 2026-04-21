# Backend (FastAPI)

This backend is designed for AI application workloads:

- Python ecosystem for model and LLM integrations
- Async API performance via FastAPI
- Clear API versioning under `/api/v1`

## Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Run

```bash
uvicorn app.main:app --reload --port 8000
```

## Endpoints

- `GET /health` - service health
- `POST /api/v1/chat` - AI chat stub response
