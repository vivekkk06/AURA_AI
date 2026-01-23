from fastapi import APIRouter, Depends
from core.dependencies import get_current_user
from db.mongo import db

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/")
def get_dashboard(user=Depends(get_current_user)):
    username = user["sub"]

    total_chats = db.chats.count_documents({"user": username})
    total_memories = db.memory.count_documents({"user": username})
    total_docs = db.documents.count_documents({"user": username})

    recent_chats_cursor = db.chats.find(
        {"user": username},
        {"_id": 0, "role": 1, "content": 1}
    ).sort("_id", -1).limit(5)

    recent_chats = list(recent_chats_cursor)

    return {
        "total_chats": total_chats,
        "total_memories": total_memories,
        "total_docs": total_docs,
        "recent_chats": recent_chats
    }
