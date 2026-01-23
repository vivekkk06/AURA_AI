import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound


def extract_video_id(url: str):
    patterns = [
        r"v=([^&]+)",
        r"youtu.be/([^?]+)",
        r"embed/([^?]+)"
    ]

    for p in patterns:
        match = re.search(p, url)
        if match:
            return match.group(1)

    return None


def get_transcript(url: str):
    video_id = extract_video_id(url)

    if not video_id:
        raise ValueError("Invalid YouTube URL")

    try:
        # ✅ NEW OFFICIAL WAY
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        # Prefer manually created English transcript
        try:
            transcript = transcript_list.find_manually_created_transcript(['en'])
        except:
            # else auto-generated English transcript
            transcript = transcript_list.find_generated_transcript(['en'])

        data = transcript.fetch()
        text = " ".join([t["text"] for t in data])
        return text

    except TranscriptsDisabled:
        raise Exception("❌ Transcripts are disabled for this video")

    except NoTranscriptFound:
        raise Exception("❌ No transcript found for this video")

    except Exception as e:
        raise Exception(f"❌ Transcript error: {str(e)}")
