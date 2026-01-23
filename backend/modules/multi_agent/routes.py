from fastapi import APIRouter, Depends
from pydantic import BaseModel
from core.dependencies import get_current_user
from .graph import run_multi_agent, run_news_agents

router = APIRouter(prefix="/agent", tags=["Multi-Agent"])

class AgentRequest(BaseModel):
    query: str

class NewsRequest(BaseModel):
    topic: str


@router.post("/run")
def run_agent(req: AgentRequest, user=Depends(get_current_user)):
    result = run_multi_agent(user["sub"], req.query)
    return {"response": result}


@router.post("/news")
def run_news(req: NewsRequest, user=Depends(get_current_user)):
    result = run_news_agents(req.topic)
    return result
