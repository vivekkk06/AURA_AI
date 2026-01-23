import os
from typing import List
from langchain_groq import ChatGroq

# =========================
# LLM CONFIG
# =========================

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# =========================
# COMMON QUESTIONS
# =========================

COMMON_QUESTIONS = [
    "Tell me about yourself.",
    "Explain your strongest skill.",
    "What is your biggest weakness?",
    "Why should we hire you?",
    "Explain a challenge you faced and how you solved it.",
    "Where do you see yourself in 3 years?",
    "Explain a project you are proud of.",
    "How do you handle failure?",
    "Explain your final year project.",
    "What do you know about this role?"
]

# =========================
# MAIN INTERVIEW SET
# =========================

def generate_interview_set(
    resume_text: str,
    skills: List[str],
    projects: list,
    weak_skills: List[str],
    missing_skills: List[str],
    role: str
):
    resume_based = ai_resume_questions(resume_text, projects, role)
    skill_based = ai_skill_questions(skills, role)
    gap_based = ai_gap_questions(weak_skills, missing_skills, role)

    return {
        "common_questions": COMMON_QUESTIONS,
        "resume_based": resume_based,
        "skill_based": skill_based,
        "gap_based": gap_based
    }

# =========================
# MORE QUESTIONS BUTTON AGENT ✅
# =========================

def generate_more_questions(stage2: dict, role: str):
    prompt = f"""
You are an advanced AI interviewer.

Candidate extracted resume data:
{stage2}

Target job role:
{role}

Generate 10 NEW interview questions (not repeating old ones).

Rules:
- Mix conceptual, project-based, and scenario-based
- Focus on role relevance
- Include expected answer points
"""

    return llm.invoke(prompt).content

# =========================
# INTERNAL AGENTS
# =========================

def ai_resume_questions(resume_text: str, projects: list, role: str):
    prompt = f"""
You are a professional technical interviewer.

Resume text:
{resume_text[:3500]}

Projects:
{projects}

Target role: {role}

Generate 5 resume-based interview questions.
Also include short expected answer points.
"""

    return llm.invoke(prompt).content


def ai_skill_questions(skills: List[str], role: str):
    prompt = f"""
You are a senior technical interviewer.

Candidate skills:
{skills}

Target role: {role}

Generate 5 deep technical questions.
Include at least one scenario-based question.
"""

    return llm.invoke(prompt).content


def ai_gap_questions(weak_skills: List[str], missing_skills: List[str], role: str):
    prompt = f"""
You are an expert interviewer.

Weak skills:
{weak_skills}

Missing core skills:
{missing_skills}

Target role: {role}

Generate 5 smart questions that test:
- fundamentals
- learning ability
- problem solving
"""

    return llm.invoke(prompt).content
