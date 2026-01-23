import os
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from db.mongo import users_col

oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/login")

SECRET = os.getenv("JWT_SECRET", "AURA_SECRET")
ALGO = "HS256"


def get_current_user(token: str = Depends(oauth2)):
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGO])
        username = payload.get("sub")

        user = users_col.find_one({"username": username})
        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        return {"sub": user["username"], "email": user["email"]}

    except:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
