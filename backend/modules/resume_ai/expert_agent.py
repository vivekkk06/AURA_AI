from langchain_groq import ChatGroq
import os
import json

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

def expert_resume_agent(stage1, extracted, role_profile, gaps, scores):
    prompt = f"""
You are an advanced Resume Intelligence System.

Analyze the resume and RETURN STRICT JSON ONLY in this format:

{{
  "overall_quality": "...",
  "strengths": ["...", "..."],
  "weaknesses": ["...", "..."],
  "ats_feedback": ["...", "..."],
  "improvement_suggestions": ["...", "..."],
  "final_verdict": "..."
}}

Resume sections: {stage1["sections"]}
Extracted data: {extracted}
Target role: {role_profile}
Skill gaps: {gaps}
Scores: {scores}

Rules:
- Do NOT add explanation
- Do NOT wrap in ``` 
- Output must be valid JSON only
"""

    response = llm.invoke(prompt).content.strip()

    try:
        return json.loads(response)
    except:
        return {
            "overall_quality": response,
            "strengths": [],
            "weaknesses": [],
            "ats_feedback": [],
            "improvement_suggestions": [],
            "final_verdict": "AI output could not be structured"
        }
