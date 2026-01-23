from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

client = MongoClient(MONGO_URI)
db = client["aura_ai"]

users_col = db["users"]
chat_col = db["chat_history"]
agent_col = db["agent_runs"]
resume_col = db["resume_sessions"]
doc_col = db["documents"]
documents_col = db["documents"]
