import db.mongo as mongo
from .vector import add_memory, search_memory as vector_search


# =========================
# STORE CHAT MEMORY
# =========================

def store_chat(user_id: str, role: str, content: str):
    # Save chat to MongoDB
    mongo.chat_col.insert_one({
        "user_id": user_id,
        "role": role,
        "content": content
    })

    # Save into vector memory (user-specific)
    add_memory(user_id, f"{role}: {content}")


# =========================
# DASHBOARD DATA
# =========================

def get_dashboard_data(user_id: str):
    total_chats = mongo.chat_col.count_documents({"user_id": user_id})
    total_docs = mongo.documents_col.count_documents({"user_id": user_id})

    recent = list(
        mongo.chat_col.find(
            {"user_id": user_id},
            {"_id": 0}
        ).sort("_id", -1).limit(10)
    )

    return {
        "total_chats": total_chats,
        "total_memories": total_chats,  # chats used as memories
        "total_docs": total_docs,
        "recent_chats": recent
    }


# =========================
# SEARCH MEMORY
# =========================

def search_memory(user_id: str, query: str):
    # Vector semantic search (user-isolated)
    return vector_search(user_id, query)
