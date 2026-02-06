import re
from youtube_transcript_api import YouTubeTranscriptApi
from .whisper_engine import transcribe_audio


def extract_video_id(url: str):
    patterns = [r"v=([^&]+)", r"youtu\.be/([^?]+)", r"embed/([^?]+)"]
    for p in patterns:
        m = re.search(p, url)
        if m:
            return m.group(1)
    return None


def get_quick_transcript(url: str):
    video_id = extract_video_id(url)
    if not video_id:
        return "Invalid YouTube URL."

    # ---------- TRY OFFICIAL CAPTIONS ----------
    try:
        t = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join(x["text"] for x in t[:60])

    except Exception as e:
        print("⚠ Caption failed:", e)

    # ---------- FALLBACK TO WHISPER ----------
    try:
        return transcribe_audio(url, seconds=120, mode="fast")

    except Exception as e:
        print("❌ Whisper failed:", e)
        return "This video has no readable captions and audio transcription failed."


def get_full_transcript(url: str):
    try:
        return transcribe_audio(url, seconds=600, mode="full")
    except Exception as e:
        print("❌ Full transcription failed:", e)
        return None
