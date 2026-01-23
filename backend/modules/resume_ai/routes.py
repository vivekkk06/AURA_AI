from fastapi import APIRouter, UploadFile, File, Depends, Form
from pydantic import BaseModel
from typing import Dict, Any
from core.dependencies import get_current_user

from .service import process_resume
from .interview_agent import generate_more_questions

router = APIRouter(prefix="/resume", tags=["Resume AI"])


# ==============================
# RESUME PROCESS PIPELINE
# ==============================

@router.post("/process")
def process(
    file: UploadFile = File(...),
    role: str = Form(...),
    user=Depends(get_current_user)
):
    return process_resume(user["sub"], file, role)


# ==============================
# MORE QUESTIONS AGENT
# ==============================

class MoreQuestionsRequest(BaseModel):
    stage2: Dict[str, Any]
    role: str


@router.post("/more-questions")
def more_questions(req: MoreQuestionsRequest, user=Depends(get_current_user)):
    # DEBUG (keep for now)
    print("✅ MORE QUESTIONS PAYLOAD:", req.dict())

    questions = generate_more_questions(req.stage2, req.role)
    return {"questions": questions}
