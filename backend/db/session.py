import os
from pymongo import MongoClient

# =========================
# DATABASE CONNECTION
# =========================

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

client = MongoClient(MONGO_URL)

db = client["aura_ai"]

users_collection = db["users"]
