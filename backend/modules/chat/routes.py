from fastapi import APIRouter, Depends
from pydantic import BaseModel
from core.dependencies import get_current_user
from modules.memory.service import store_chat
from modules.multi_agent.graph import run_multi_agent

router = APIRouter(prefix="/chat", tags=["Chat"])

class ChatRequest(BaseModel):
    message: str

@router.post("/")
def chat(req: ChatRequest, user=Depends(get_current_user)):
    user_id = user["sub"]

    reply = run_multi_agent(user_id, req.message)

    store_chat(user_id, "user", req.message)
    store_chat(user_id, "assistant", reply)

    return {"reply": reply}
