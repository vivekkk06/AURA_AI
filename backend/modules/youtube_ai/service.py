from .transcript import (
    get_quick_transcript,
    get_full_transcript,
    extract_video_id
)
from langchain_groq import ChatGroq
from db.mongo import youtube_col
from datetime import datetime
from bson import ObjectId
import os


# ============================================================
# ---------------- LLM CONFIG ---------------- #
# ============================================================

llm_fast = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

llm_full = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2,
    groq_api_key=os.getenv("GROQ_API_KEY")
)


# ============================================================
# ---------------- HELPER: SERIALIZE MONGO ---------------- #
# ============================================================

def serialize_doc(doc: dict):
    """
    Convert MongoDB document into JSON-safe dictionary.
    """
    if not doc:
        return None

    clean = {}
    for key, value in doc.items():
        if isinstance(value, ObjectId):
            clean[key] = str(value)
        else:
            clean[key] = value

    return clean


# ============================================================
# ---------------- FULL SUMMARY (BACKGROUND TASK) ------------ #
# ============================================================

def refine_summary(url: str):
    try:
        youtube_col.update_one(
            {"url": url},
            {"$set": {
                "stage": "full_summary",
                "updated_at": datetime.utcnow()
            }}
        )

        content, metadata = get_full_transcript(url)

        if not content:
            youtube_col.update_one(
                {"url": url},
                {"$set": {
                    "status": "error",
                    "stage": "error",
                    "updated_at": datetime.utcnow()
                }}
            )
            return

        prompt = f"""
Create a detailed structured summary.

{content}

Provide:
- Short summary
- Key points
- Important insights
- Final takeaway
"""

        result = llm_full.invoke(prompt).content

        youtube_col.update_one(
            {"url": url},
            {"$set": {
                "full_summary": result,
                "status": "done",
                "stage": "completed",
                "updated_at": datetime.utcnow()
            }}
        )

    except Exception as e:
        youtube_col.update_one(
            {"url": url},
            {"$set": {
                "status": "error",
                "stage": "error",
                "error": str(e),
                "updated_at": datetime.utcnow()
            }}
        )


# ============================================================
# ---------------- MAIN SUMMARIZE FUNCTION ------------------- #
# ============================================================

def summarize_youtube(url: str, bg):

    video_id = extract_video_id(url)

    if not video_id:
        return {
            "status": "error",
            "stage": "error",
            "summary": "Invalid YouTube URL",
            "metadata": None
        }

    clean_url = f"https://youtu.be/{video_id}"

    existing = youtube_col.find_one({"url": clean_url})

    # ✅ If full summary already exists → return safe response
    if existing and existing.get("full_summary"):
        existing = serialize_doc(existing)

        return {
            "status": existing.get("status"),
            "stage": existing.get("stage"),
            "summary": existing.get("full_summary"),
            "metadata": existing.get("metadata")
        }

    # Fetch content + metadata
    content, metadata = get_quick_transcript(clean_url)

    if not content:
        return {
            "status": "error",
            "stage": "error",
            "summary": "Failed to fetch video data",
            "metadata": None
        }

    # Generate quick summary
    quick_summary = llm_fast.invoke(
        f"Give a quick high-level summary:\n\n{content[:2000]}"
    ).content

    # Save to Mongo
    youtube_col.update_one(
        {"url": clean_url},
        {"$set": {
            "url": clean_url,
            "status": "processing",
            "stage": "quick_summary",
            "quick_summary": quick_summary,
            "metadata": metadata,
            "updated_at": datetime.utcnow()
        }},
        upsert=True
    )

    # Background full summary
    if bg:
        bg.add_task(refine_summary, clean_url)

    return {
        "status": "processing",
        "stage": "quick_summary",
        "summary": quick_summary,
        "metadata": metadata
    }


# ============================================================
# ---------------- STATUS CHECK FUNCTION --------------------- #
# ============================================================

def get_summary(url: str):

    video_id = extract_video_id(url)

    if not video_id:
        return {
            "status": "error",
            "stage": "error",
            "summary": "Invalid URL",
            "metadata": None
        }

    clean_url = f"https://youtu.be/{video_id}"

    doc = youtube_col.find_one({"url": clean_url})

    if not doc:
        return {
            "status": "processing",
            "stage": "quick_summary",
            "summary": "Processing...",
            "metadata": None
        }

    # 🔥 Convert Mongo doc safely
    doc = serialize_doc(doc)

    return {
        "status": doc.get("status"),
        "stage": doc.get("stage"),
        "summary": doc.get("full_summary") or doc.get("quick_summary"),
        "metadata": doc.get("metadata")
    }
from .whisper_engine import full_model
import os
import uuid
import shutil


# ============================================================
# ---------------- AUDIO UPLOAD SUMMARY ----------------------
# ============================================================

def summarize_uploaded_audio(file, bg=None):
    """
    Handles manual audio upload if YouTube has no captions.
    """

    try:
        # ----------------------------------------------------
        # Validate File
        # ----------------------------------------------------
        if not file:
            return {
                "status": "error",
                "stage": "error",
                "summary": "No file uploaded",
                "metadata": None
            }

        # ----------------------------------------------------
        # Save File Temporarily
        # ----------------------------------------------------
        temp_filename = f"uploaded_{uuid.uuid4().hex}_{file.filename}"

        with open(temp_filename, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # ----------------------------------------------------
        # Transcribe Using Whisper (small model)
        # ----------------------------------------------------
        segments, _ = full_model.transcribe(
            temp_filename,
            vad_filter=True
        )

        transcript_text = " ".join(seg.text for seg in segments).strip()

        if not transcript_text:
            os.remove(temp_filename)
            return {
                "status": "error",
                "stage": "error",
                "summary": "Transcription failed",
                "metadata": None
            }

        # ----------------------------------------------------
        # Generate Summary Using Groq
        # ----------------------------------------------------
        prompt = f"""
Create a detailed structured summary of the following transcript:

{transcript_text[:5000]}

Provide:
- Short summary
- Key points
- Important insights
- Final takeaway
"""

        summary = llm_full.invoke(prompt).content

        # ----------------------------------------------------
        # Save to MongoDB
        # ----------------------------------------------------
        youtube_col.insert_one({
            "url": f"uploaded_audio_{uuid.uuid4().hex}",
            "status": "done",
            "stage": "completed",
            "full_summary": summary,
            "metadata": {
                "title": file.filename,
                "channel": "Uploaded Audio",
                "thumbnail": None,
                "views": None,
                "likes": None,
                "duration": None,
                "subscribers": None
            },
            "created_at": datetime.utcnow()
        })

        # ----------------------------------------------------
        # Cleanup File
        # ----------------------------------------------------
        try:
            os.remove(temp_filename)
        except Exception:
            pass

        return {
            "status": "done",
            "stage": "completed",
            "summary": summary,
            "metadata": {
                "title": file.filename,
                "channel": "Uploaded Audio"
            }
        }

    except Exception as e:

        try:
            if os.path.exists(temp_filename):
                os.remove(temp_filename)
        except Exception:
            pass

        return {
            "status": "error",
            "stage": "error",
            "summary": f"Audio processing failed: {str(e)}",
            "metadata": None
        }
