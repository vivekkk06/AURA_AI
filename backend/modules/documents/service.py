import os
import uuid

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from modules.memory.vector import add_doc_chunks, search_doc_memory
from db.mongo import documents_col


UPLOAD_DIR = "uploads/docs"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# =========================
# PROCESS DOCUMENT
# =========================

def process_document(user_id: str, file):
    doc_id = str(uuid.uuid4())
    file_path = f"{UPLOAD_DIR}/{user_id}_{doc_id}.pdf"

    # Save PDF
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    # Load PDF
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(docs)

    texts = [d.page_content for d in chunks]

    # ✅ Store chunks in FAISS (batch-safe)
    add_doc_chunks(
        user_id=user_id,
        doc_id=doc_id,
        chunks=texts
    )

    # ✅ Store document record in MongoDB (dashboard + tracking)
    documents_col.insert_one({
        "user_id": user_id,
        "doc_id": doc_id,
        "filename": file.filename,
        "chunks": len(texts)
    })

    return {
        "doc_id": doc_id,
        "filename": file.filename,
        "chunks": len(texts)
    }


# =========================
# ASK DOCUMENT
# =========================

def ask_document(user_id: str, doc_id: str, question: str):
    results = search_doc_memory(user_id, doc_id, question)

    if not results:
        return None

    # Return top relevant chunks as context
    return "\n\n".join(results[:5])
