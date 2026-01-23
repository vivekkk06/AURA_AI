import os
from datetime import datetime, timedelta
from jose import jwt

SECRET = os.getenv("JWT_SECRET", "AURA_SECRET")
ALGO = "HS256"

def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode["exp"] = datetime.utcnow() + timedelta(days=7)
    return jwt.encode(to_encode, SECRET, algorithm=ALGO)
