# Backend (FastAPI)

This backend is designed for AI application workloads:

- Python ecosystem for model and LLM integrations
- Async API performance via FastAPI
- Clear API versioning under `/api/v1`

## Setup

```bash
cd backend
# install uv once (https://docs.astral.sh/uv/)
# curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
cp .env.example .env
```

## Run

```bash
uv run uvicorn app.main:app --reload --port 8000
```

## Endpoints

- `GET /health` - service health
- `POST /api/v1/chat` - AI chat stub response
- `POST /api/v1/agent` - Agno-powered agent response (requires `OPENAI_API_KEY`)

## Agno agentic framework

This project includes a starter Agno agent integration.

1. Set your OpenAI key in `.env`:

```bash
OPENAI_API_KEY=your_key_here
AGNO_MODEL_ID=gpt-4o-mini
AGNO_ENABLE_WEB_SEARCH=true
```

2. Call the endpoint:

```bash
curl -X POST http://localhost:8000/api/v1/agent \
  -H "Content-Type: application/json" \
  -d '{"message":"Give me 3 startup ideas in AI healthcare"}'
```

## Free web search integration (MCP-style tool use)

The Agno agent is configured with `DuckDuckGoTools`, a free web search toolkit.

- No API key required for search
- Controlled by `AGNO_ENABLE_WEB_SEARCH` in `.env`
- The agent can search the web for up-to-date answers when needed
