from fastapi import APIRouter, HTTPException, Form
from core.security import create_access_token
from .service import send_otp, verify_otp, create_user, authenticate

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/send-otp")
def send(email: str = Form(...)):
    send_otp(email)
    return {"msg": "OTP sent"}


@router.post("/verify-otp")
def verify(
    email: str = Form(...),
    otp: str = Form(...),
    username: str = Form(...),
    password: str = Form(...)
):
    if not verify_otp(email, otp):
        raise HTTPException(400, "Invalid OTP")

    create_user(email, username, password)
    return {"msg": "Account created"}


@router.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    user = authenticate(username, password)
    if not user:
        raise HTTPException(401, "Invalid credentials")

    token = create_access_token({"sub": user["username"]})
    return {"access_token": token}
