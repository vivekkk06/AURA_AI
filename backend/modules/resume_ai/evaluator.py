import os, json, re
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2,
    groq_api_key=os.getenv("GROQ_API_KEY")
)


def expert_resume_agent(stage1: dict, extracted: dict, role_profile: dict, gaps: dict, scores: dict):
    prompt = f"""
You are an advanced Resume Intelligence AI used by recruiters.

RESUME SECTIONS:
{stage1["sections"]}

RESUME TEXT (partial):
{stage1["raw_text"][:3500]}

EXTRACTED DATA:
{extracted}

TARGET ROLE PROFILE:
{role_profile}

SKILL GAPS:
{gaps}

SCORES:
{scores}

Generate STRICT JSON only:

{{
  "overall_quality": "...",
  "strengths": ["...", "..."],
  "weaknesses": ["...", "..."],
  "ats_feedback": ["...", "..."],
  "improvement_suggestions": ["...", "..."],
  "final_verdict": "..."
}}
"""

    raw = llm.invoke(prompt).content

    # ---------- SAFE JSON EXTRACTION ----------
    try:
        json_text = re.search(r"\{.*\}", raw, re.S).group()
        return json.loads(json_text)
    except:
        return {
            "overall_quality": raw,
            "strengths": [],
            "weaknesses": [],
            "ats_feedback": [],
            "improvement_suggestions": [],
            "final_verdict": "AI parsing fallback"
        }
