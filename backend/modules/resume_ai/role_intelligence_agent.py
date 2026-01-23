from langchain_groq import ChatGroq
import os, json

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

def analyze_role_with_ai(role: str):
    prompt = f"""
You are a senior hiring expert.

Target role: {role}

Return STRICT JSON only:

{{
 "role_summary": "...",
 "core_skills": [],
 "tools": [],
 "nice_to_have": [],
 "projects_expected": [],
 "experience_focus": []
}}
"""

    res = llm.invoke(prompt).content.strip()

    try:
        return json.loads(res)
    except:
        return {
            "role_summary": "",
            "core_skills": [],
            "tools": [],
            "nice_to_have": [],
            "projects_expected": [],
            "experience_focus": []
        }