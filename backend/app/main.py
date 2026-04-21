from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    return {"status": "ok"}


@app.post("/api/v1/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    # Placeholder AI response until an LLM provider is integrated.
    generated = (
        "Backend received your message: "
        f"\"{request.message}\". Connect an LLM provider in this endpoint."
    )
    return ChatResponse(response=generated)
