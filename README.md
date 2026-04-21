# aura

FastAPI backend starter for an AI application.

## Quick start

```bash
# install uv once (if needed): https://docs.astral.sh/uv/getting-started/installation/
uv sync
cp .env.example .env
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Project structure

- `app/` - FastAPI application modules
- `pyproject.toml` - Python project/dependency configuration
- `uv.lock` - uv lockfile

## API endpoints

- `GET /health` - service health
- `POST /api/v1/chat` - chat stub
- `POST /api/v1/agent` - Agno agent response
- `GET /stream` - HTML output route
