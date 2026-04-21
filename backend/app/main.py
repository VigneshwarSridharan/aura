from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from app.config import settings
from app.schemas import ChatRequest, ChatResponse


app = FastAPI(
    title="AI App Backend",
    version="0.1.0",
    description="FastAPI backend for an AI-enabled application.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok 123"}


@app.post("/api/v1/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    # Placeholder AI response until an LLM provider is integrated.
    generated = (
        "Backend received your message: "
        f"\"{request.message}\". Connect an LLM provider in this endpoint."
    )
    return ChatResponse(response=generated)


@app.get("/stream", response_class=HTMLResponse)
def stream_page() -> str:
    return """<!doctype html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
  </head>
  <body>
    <h1 class="text-3xl font-bold underline">
      Hello world!
    </h1>
  </body>
</html>"""
