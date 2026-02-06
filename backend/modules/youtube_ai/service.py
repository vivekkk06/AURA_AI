from .transcript import get_quick_transcript, get_full_transcript
from langchain_groq import ChatGroq
from db.mongo import youtube_col
from datetime import datetime
import os

llm_fast = ChatGroq(model="llama-3.1-8b-instant", temperature=0.2, groq_api_key=os.getenv("GROQ_API_KEY"))
llm_full = ChatGroq(model="llama-3.1-8b-instant", temperature=0.2, groq_api_key=os.getenv("GROQ_API_KEY"))


def refine_summary(url: str):
    try:
        # 🧠 FULL SUMMARY STAGE
        youtube_col.update_one(
            {"url": url},
            {"$set": {"stage": "full_summary", "updated_at": datetime.utcnow()}}
        )

        transcript = get_full_transcript(url)[:3000]

        prompt = f"""
Create a detailed structured summary.

Transcript:
{transcript}

Give:
- Short summary
- Key points
- Important concepts
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
            {"$set": {"status": "error", "stage": "error", "error": str(e)}}
        )


def summarize_youtube(url: str, bg):
    doc = youtube_col.find_one({"url": url})
    if doc and doc.get("full_summary"):
        return {"status": "done", "summary": doc["full_summary"], "stage": "completed"}

    # 🔊 TRANSCRIBING
    youtube_col.update_one(
        {"url": url},
        {"$set": {
            "url": url,
            "status": "processing",
            "stage": "transcribing",
            "updated_at": datetime.utcnow()
        }},
        upsert=True
    )

    quick_text = get_quick_transcript(url)[:2000]

    # ⚡ QUICK SUMMARY
    youtube_col.update_one(
        {"url": url},
        {"$set": {"stage": "quick_summary", "updated_at": datetime.utcnow()}}
    )

    quick_prompt = f"Give a quick high-level summary:\n{quick_text}"
    quick_summary = llm_fast.invoke(quick_prompt).content

    youtube_col.update_one(
        {"url": url},
        {"$set": {"quick_summary": quick_summary, "updated_at": datetime.utcnow()}}
    )

    bg.add_task(refine_summary, url)

    return {
        "status": "processing",
        "summary": quick_summary,
        "stage": "quick_summary",
        "message": "Quick summary ready. Full summary processing..."
    }


def get_summary(url: str):
    doc = youtube_col.find_one({"url": url})
    if not doc:
        return {"status": "processing", "stage": "transcribing", "summary": "Processing..."}

    return {
        "status": doc.get("status"),
        "stage": doc.get("stage"),
        "summary": doc.get("full_summary") or doc.get("quick_summary")
    }
