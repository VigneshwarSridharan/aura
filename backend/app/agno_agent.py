from agno.agent import Agent
from agno.models.openai import OpenAIChat

from app.config import settings


HTML_INSTRUCTIONS = """You are an HTML UI generator.

Return ONLY a complete, valid HTML5 document. Do not return markdown, JSON, explanations, or code fences.

Requirements:
- Start with <!doctype html>.
- Include <html>, <head>, and <body>.
- In <head>, include:
  - <meta charset="UTF-8" />
  - <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  - <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
- Use semantic, accessible HTML (headings, paragraphs, lists, buttons, labels where needed).
- Style using Tailwind utility classes.
- Keep layout clean and responsive with a centered container.
- If external libraries are needed, use trusted CDNs only and keep them minimal.
- Never include inline JavaScript that executes arbitrary user input.
- Never include markdown code fences.
- Ensure the output is directly renderable in a browser as-is.
"""


def run_agent_prompt(message: str) -> str:
    if not settings.openai_api_key:
        raise ValueError("OPENAI_API_KEY is not configured.")

    agent = Agent(
        model=OpenAIChat(
            id=settings.openai_model_id,
            api_key=settings.openai_api_key,
        ),
        markdown=False,
        instructions=HTML_INSTRUCTIONS,
    )
    response = agent.run(message)
    content = getattr(response, "content", None)
    if isinstance(content, str) and "<html" in content.lower():
        return content

    # Safe fallback in case the model returns plain text.
    text = content if isinstance(content, str) else str(response)
    return f"""<!doctype html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
  </head>
  <body>
    <h1 class="text-3xl font-bold underline">
      Agent Response
    </h1>
    <p class="mt-4 text-lg">
      {text}
    </p>
  </body>
</html>"""
