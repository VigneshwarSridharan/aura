from agno.agent import Agent
from agno.models.openai import OpenAIChat

from app.config import settings


def run_agent_prompt(message: str) -> str:
    if not settings.openai_api_key:
        raise ValueError("OPENAI_API_KEY is not configured.")

    agent = Agent(
        model=OpenAIChat(
            id=settings.openai_model_id,
            api_key=settings.openai_api_key,
        ),
        markdown=True,
    )
    response = agent.run(message)
    content = getattr(response, "content", None)
    if isinstance(content, str):
        return content
    return str(response)
