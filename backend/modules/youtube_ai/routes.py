from fastapi import APIRouter, Depends
from pydantic import BaseModel
from core.dependencies import get_current_user
from .service import summarize_youtube

router = APIRouter(prefix="/youtube", tags=["YouTube AI"])


class YoutubeRequest(BaseModel):
    url: str


@router.post("/summarize")
def youtube_summary(req: YoutubeRequest, user=Depends(get_current_user)):
    return summarize_youtube(req.url)
