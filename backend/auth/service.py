import os, random, smtplib
from email.message import EmailMessage
from passlib.context import CryptContext
from db.mongo import users_col

pwd = CryptContext(schemes=["argon2"], deprecated="auto")


OTP_STORE = {}

EMAIL = os.getenv("EMAIL_USER")
PASS = os.getenv("EMAIL_PASS")


def send_otp(email: str):
    otp = str(random.randint(100000, 999999))
    OTP_STORE[email] = otp

    msg = EmailMessage()
    msg["Subject"] = "AURA AI - OTP Verification"
    msg["From"] = EMAIL
    msg["To"] = email
    msg.set_content(f"Your OTP is: {otp}")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, PASS)
        server.send_message(msg)


def verify_otp(email: str, otp: str):
    return OTP_STORE.get(email) == otp


def create_user(email, username, password):
    users_col.insert_one({
        "email": email,
        "username": username,
        "password": pwd.hash(password)
    })
    OTP_STORE.pop(email, None)


def authenticate(username, password):
    user = users_col.find_one({"username": username})
    if not user:
        return None
    if not pwd.verify(password, user["password"]):

        return None
    return user
