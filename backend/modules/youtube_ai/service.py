import os
from langchain_groq import ChatGroq
from .transcript import get_transcript

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
    groq_api_key=os.getenv("GROQ_API_KEY")
)


def summarize_youtube(url: str):
    transcript = get_transcript(url)

    prompt = f"""
You are an expert AI summarizer.

Transcript:
{transcript[:12000]}

Generate:
1. Short professional summary
2. Bullet key points
3. Actionable takeaways
"""

    result = llm.invoke(prompt).content

    return {
        "transcript_preview": transcript[:1000],
        "summary": result
    }
