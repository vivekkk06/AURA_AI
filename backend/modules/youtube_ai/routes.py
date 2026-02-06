from fastapi import APIRouter, Depends, BackgroundTasks
from pydantic import BaseModel
from core.dependencies import get_current_user
from .service import summarize_youtube, get_summary

router = APIRouter(prefix="/youtube", tags=["YouTube AI"])

class YouTubeRequest(BaseModel):
    url: str

@router.post("/summarize")
def youtube_summary(req: YouTubeRequest, bg: BackgroundTasks, user=Depends(get_current_user)):
    return summarize_youtube(req.url, bg)

@router.get("/status")
def youtube_status(url: str, user=Depends(get_current_user)):
    return get_summary(url)
