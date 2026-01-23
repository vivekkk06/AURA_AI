from fastapi import APIRouter, Depends
from pydantic import BaseModel
from core.dependencies import get_current_user
from modules.multi_agent.graph import run_news_agents

router = APIRouter(prefix="/news", tags=["News Research Agent"])


class NewsRequest(BaseModel):
    topic: str


@router.post("/research")
def research_news(req: NewsRequest, user=Depends(get_current_user)):
    result = run_news_agents(req.topic)
    return result
