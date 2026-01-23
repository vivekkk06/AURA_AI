import os, smtplib
from email.message import EmailMessage

EMAIL = os.getenv("EMAIL_USER")
PASS = os.getenv("EMAIL_PASS")

msg = EmailMessage()
msg["Subject"] = "Test Mail"
msg["From"] = EMAIL
msg["To"] = EMAIL
msg.set_content("Hello from AURA")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(EMAIL, PASS)
    server.send_message(msg)

print("MAIL SENT")
