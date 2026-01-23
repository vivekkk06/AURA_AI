from fastapi import APIRouter, UploadFile, File, Depends
from pydantic import BaseModel

from core.dependencies import get_current_user
from .service import process_document, ask_document
from modules.multi_agent.graph import llm_answer_from_context

router = APIRouter(prefix="/docs", tags=["Documents"])


# =========================
# REQUEST MODEL
# =========================

class AskDocRequest(BaseModel):
    doc_id: str
    question: str


# =========================
# UPLOAD DOCUMENT
# =========================

@router.post("/upload")
def upload_doc(
    file: UploadFile = File(...),
    user=Depends(get_current_user)
):
    return process_document(user["sub"], file)


# =========================
# ASK DOCUMENT
# =========================

@router.post("/ask")
def ask_doc(
    req: AskDocRequest,
    user=Depends(get_current_user)
):
    # Retrieve relevant chunks from FAISS
    context = ask_document(user["sub"], req.doc_id, req.question)

    if not context:
        return {"answer": "❌ Not present in the document."}

    # Generate final answer from LLM using retrieved context
    answer = llm_answer_from_context(context, req.question)

    return {"answer": answer}
