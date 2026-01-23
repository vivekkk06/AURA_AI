import os
import uuid

from .stage1_document import parse_resume_pdf
from .stage2_extraction import extract_information
from .stage3_embeddings import store_resume_embedding

from .role_intelligence_agent import analyze_role_with_ai
from .gap_engine import compare_resume_vs_role
from .scoring_engine import compute_scores
from .interview_agent import generate_interview_set
from .expert_agent import expert_resume_agent


UPLOAD_DIR = "uploads/resumes"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def process_resume(user_id: str, file, role: str):
    resume_id = str(uuid.uuid4())
    path = f"{UPLOAD_DIR}/{user_id}_{resume_id}.pdf"

    # ---------------- SAVE FILE ----------------
    with open(path, "wb") as f:
        f.write(file.file.read())

    # ---------------- STAGE 1: DOCUMENT INTELLIGENCE ----------------
    stage1 = parse_resume_pdf(path)

    # ---------------- STAGE 2: INFORMATION EXTRACTION ----------------
    extracted = extract_information(stage1["raw_text"])

    # ---------------- STAGE 3: VECTOR STORAGE ----------------
    store_resume_embedding(
        user_id=user_id,
        resume_text=stage1["raw_text"],
        meta={"resume_id": resume_id, "type": "resume"}
    )

    # ---------------- STAGE 4: ROLE INTELLIGENCE ----------------
    role_profile = analyze_role_with_ai(role)

    # ---------------- STAGE 5: GAP ENGINE ----------------
    gaps = compare_resume_vs_role(extracted, role_profile)

    # ---------------- STAGE 6: SCORING ----------------
    scores = compute_scores(stage1, extracted, gaps)

    # ---------------- STAGE 7: INTERVIEW AGENTS ✅ FIXED ----------------
    interview = generate_interview_set(
        stage1["raw_text"],        # resume_text
        extracted["skills"],       # skills
        extracted["projects"],     # projects
        gaps["weak"],              # weak_skills
        gaps["missing_core"],      # missing_skills
        role                       # role
    )

    # ---------------- STAGE 8: EXPERT AI REPORT ----------------
    expert_report = expert_resume_agent(
        stage1=stage1,
        extracted=extracted,
        role_profile=role_profile,
        gaps=gaps,
        scores=scores
    )

    # ---------------- FINAL RESPONSE ----------------
    return {
        "resume_id": resume_id,
        "role": role,

        "sections": stage1["sections"],
        "skills": extracted["skills"],
        "experience_years": extracted["experience_years"],
        "projects": extracted["projects"],

        "role_profile": role_profile,
        "skill_gaps": gaps,
        "scores": scores,

        "interview_questions": interview,
        "ai_summary": expert_report,

        # internal (for more-questions, debugging, etc.)
        "stage1": stage1,
        "stage2": extracted
    }
