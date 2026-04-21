from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


class AgentRequest(BaseModel):
    message: str


class AgentResponse(BaseModel):
    response: str
