import os
import requests
from urllib.parse import urlparse, parse_qs
import re

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")


# ============================================================
# ---------------- VIDEO ID EXTRACT ---------------- #
# ============================================================

def extract_video_id(url: str):
    """
    Extract clean video ID from any YouTube URL format.

    Handles:
    - youtube.com/watch?v=ID
    - youtu.be/ID
    - youtube.com/watch?v=ID&list=...
    """

    if not url:
        return None

    try:
        parsed = urlparse(url)

        # youtube.com/watch?v=VIDEO_ID
        if "youtube.com" in parsed.netloc:
            query = parse_qs(parsed.query)
            return query.get("v", [None])[0]

        # youtu.be/VIDEO_ID
        if "youtu.be" in parsed.netloc:
            return parsed.path.strip("/")

    except Exception:
        return None

    return None


# ============================================================
# ---------------- ISO 8601 DURATION FORMAT ---------------- #
# ============================================================

def format_duration(duration: str):
    """
    Convert ISO 8601 duration (PT4M13S) to 4:13 format
    """

    if not duration:
        return None

    pattern = re.compile(
        r"PT"
        r"(?:(\d+)H)?"
        r"(?:(\d+)M)?"
        r"(?:(\d+)S)?"
    )

    match = pattern.match(duration)

    if not match:
        return duration

    hours = int(match.group(1)) if match.group(1) else 0
    minutes = int(match.group(2)) if match.group(2) else 0
    seconds = int(match.group(3)) if match.group(3) else 0

    if hours:
        return f"{hours}:{minutes:02d}:{seconds:02d}"

    return f"{minutes}:{seconds:02d}"


# ============================================================
# ---------------- FETCH FULL VIDEO DATA ---------------- #
# ============================================================

def fetch_video_data(video_id: str):

    if not YOUTUBE_API_KEY or not video_id:
        return None

    try:
        # ---------------- VIDEO DETAILS ---------------- #
        video_url = "https://www.googleapis.com/youtube/v3/videos"

        video_params = {
            "part": "snippet,statistics,contentDetails",
            "id": video_id,
            "key": YOUTUBE_API_KEY
        }

        video_res = requests.get(video_url, params=video_params, timeout=10)
        video_res.raise_for_status()

        video_json = video_res.json()

        if not video_json.get("items"):
            return None

        video = video_json["items"][0]

        snippet = video.get("snippet", {})
        stats = video.get("statistics", {})
        details = video.get("contentDetails", {})

        # ---------------- CHANNEL DETAILS ---------------- #
        subscribers = None
        channel_id = snippet.get("channelId")

        if channel_id:
            channel_url = "https://www.googleapis.com/youtube/v3/channels"

            channel_params = {
                "part": "statistics",
                "id": channel_id,
                "key": YOUTUBE_API_KEY
            }

            channel_res = requests.get(channel_url, params=channel_params, timeout=10)
            channel_res.raise_for_status()

            channel_json = channel_res.json()

            if channel_json.get("items"):
                subscribers = (
                    channel_json["items"][0]
                    .get("statistics", {})
                    .get("subscriberCount")
                )

        # ---------------- SAFE THUMBNAIL ---------------- #
        thumbnail = None
        thumbnails = snippet.get("thumbnails", {})

        for quality in ["high", "medium", "default"]:
            if quality in thumbnails:
                thumbnail = thumbnails[quality].get("url")
                break

        return {
            "video_id": video_id,
            "title": snippet.get("title"),
            "description": snippet.get("description"),
            "channel": snippet.get("channelTitle"),
            "thumbnail": thumbnail,
            "views": stats.get("viewCount"),
            "likes": stats.get("likeCount"),
            "duration": format_duration(details.get("duration")),
            "subscribers": subscribers
        }

    except Exception:
        return None


# ============================================================
# ---------------- QUICK CONTENT ---------------- #
# ============================================================

def get_quick_transcript(url: str):
    """
    Returns:
        content_text (str),
        metadata_dict (dict)
    """

    video_id = extract_video_id(url)

    if not video_id:
        return None, None

    data = fetch_video_data(video_id)

    if not data:
        return None, None

    content = f"""
Title: {data.get('title')}

Channel: {data.get('channel')}

Description:
{data.get('description')}
"""

    return content.strip(), data


# ============================================================
# ---------------- FULL CONTENT ---------------- #
# ============================================================

def get_full_transcript(url: str):
    """
    Currently same as quick transcript.
    Kept separate for future expansion.
    """

    return get_quick_transcript(url)
