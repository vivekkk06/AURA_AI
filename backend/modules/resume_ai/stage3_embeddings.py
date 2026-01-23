import os
import threading
from typing import Dict

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# =========================
# CONFIG
# =========================

BASE_PATH = "data/resume_vectors"
os.makedirs(BASE_PATH, exist_ok=True)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

stores = {}
lock = threading.Lock()


# =========================
# LOAD / CREATE STORE
# =========================

def get_store(user_id: str) -> FAISS:
    path = f"{BASE_PATH}/{user_id}"
    os.makedirs(path, exist_ok=True)

    if user_id not in stores:
        if os.path.exists(path + "/index.faiss"):
            stores[user_id] = FAISS.load_local(
                path,
                embeddings,
                allow_dangerous_deserialization=True
            )
        else:
            stores[user_id] = FAISS.from_texts(
                ["resume system initialized"],
                embeddings,
                metadatas=[{"type": "system"}]
            )
            stores[user_id].save_local(path)

    return stores[user_id]


# =========================
# STORE RESUME EMBEDDING
# =========================

def store_resume_embedding(user_id: str, resume_text: str, meta: Dict):
    with lock:
        db = get_store(user_id)

        metadata = {
            "user_id": user_id,
            "type": "resume",
            **meta
        }

        db.add_texts([resume_text], metadatas=[metadata])
        db.save_local(f"{BASE_PATH}/{user_id}")


# =========================
# OPTIONAL: SEARCH RESUMES
# =========================

def search_resume_embeddings(user_id: str, query: str, k=3):
    db = get_store(user_id)
    docs = db.similarity_search(query, k=k)

    results = []
    for d in docs:
        if d.metadata.get("type") == "resume":
            results.append(d.page_content)

    return results
