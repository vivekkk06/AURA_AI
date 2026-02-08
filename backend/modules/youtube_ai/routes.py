from fastapi import APIRouter, Depends, BackgroundTasks, UploadFile, File
from pydantic import BaseModel
from core.dependencies import get_current_user
from .service import (
    summarize_youtube,
    get_summary,
    summarize_uploaded_audio
)

# ============================================================
# Router Configuration
# ============================================================

router = APIRouter(
    prefix="/youtube",
    tags=["YouTube AI"]
)


# ============================================================
# Request Model
# ============================================================

class YouTubeRequest(BaseModel):
    url: str


# ============================================================
# Summarize Endpoint (YouTube URL)
# ============================================================

@router.post("/summarize")
def youtube_summary(
    req: YouTubeRequest,
    bg: BackgroundTasks,
    user=Depends(get_current_user)
):
    """
    Generate quick summary immediately.
    Full summary runs in background.
    """
    return summarize_youtube(req.url, bg)


# ============================================================
# Status Endpoint
# ============================================================

@router.get("/status")
def youtube_status(
    url: str,
    user=Depends(get_current_user)
):
    """
    Fetch processing status or completed summary.
    """
    return get_summary(url)


# ============================================================
# Upload Audio Fallback Endpoint
# ============================================================

@router.post("/upload-audio")
def upload_audio(
    file: UploadFile = File(...),
    bg: BackgroundTasks = None,
    user=Depends(get_current_user)
):
    """
    If YouTube video has no captions,
    user can upload audio/video file manually.
    """
    return summarize_uploaded_audio(file, bg)
