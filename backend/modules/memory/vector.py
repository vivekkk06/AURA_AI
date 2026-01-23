import os
import threading
from typing import List

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# =========================
# CONFIG
# =========================

BASE_PATH = "data/vector_store"
os.makedirs(BASE_PATH, exist_ok=True)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# In-memory loaded stores
stores = {}

# Thread lock to prevent FAISS corruption
lock = threading.Lock()


# =========================
# CORE STORE HANDLER
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
                ["system initialized"],
                embeddings,
                metadatas=[{"type": "system"}]
            )
            stores[user_id].save_local(path)

    return stores[user_id]


# =========================
# CHAT MEMORY
# =========================

def add_memory(user_id: str, text: str):
    with lock:
        db = get_store(user_id)

        db.add_texts(
            [text],
            metadatas=[{
                "user_id": user_id,
                "type": "chat"
            }]
        )

        db.save_local(f"{BASE_PATH}/{user_id}")


def search_memory(user_id: str, query: str, k=4):
    db = get_store(user_id)
    docs = db.similarity_search(query, k=k)

    return [d.page_content for d in docs]


# =========================
# DOCUMENT MEMORY
# =========================

def add_doc_chunks(user_id: str, doc_id: str, chunks: List[str]):
    if not chunks:
        return

    with lock:
        db = get_store(user_id)

        metadatas = [{
            "user_id": user_id,
            "doc_id": doc_id,
            "type": "doc"
        } for _ in chunks]

        db.add_texts(chunks, metadatas=metadatas)
        db.save_local(f"{BASE_PATH}/{user_id}")


def search_doc_memory(user_id: str, doc_id: str, query: str, k=8):
    db = get_store(user_id)
    docs = db.similarity_search(query, k=k)

    results = []
    for d in docs:
        meta = d.metadata or {}

        if (
            meta.get("type") == "doc" and
            meta.get("user_id") == user_id and
            meta.get("doc_id") == doc_id
        ):
            results.append(d.page_content)

    return results
