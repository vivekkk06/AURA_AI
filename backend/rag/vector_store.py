from langchain_community.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
import faiss
import pickle


model = SentenceTransformer("all-MiniLM-L6-v2")

def build_index(texts, path):
    vectors = model.encode(texts)
    index = faiss.IndexFlatL2(len(vectors[0]))
    index.add(vectors)
    pickle.dump((index, texts), open(path, "wb"))

def search(query, path):
    index, texts = pickle.load(open(path, "rb"))
    qv = model.encode([query])
    _, idx = index.search(qv, 3)
    return [texts[i] for i in idx[0]]

