import streamlit as st
import requests

# ---------------- CONFIG ----------------
st.set_page_config("Register | AURA", layout="centered")

# ---------------- GLOBAL STYLE ----------------
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top left, #020617, #020617);
    color: white;
}

.card {
    background: rgba(15,23,42,0.9);
    padding: 35px;
    border-radius: 24px;
    border: 1px solid rgba(148,163,184,0.15);
    box-shadow: 0 0 40px rgba(56,189,248,0.08);
    max-width: 480px;
    margin: auto;
}

.title {
    font-size: 36px;
    font-weight: 800;
    text-align: center;
}

.subtitle {
    color: #94a3b8;
    text-align: center;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "otp_sent" not in st.session_state:
    st.session_state.otp_sent = False

# ---------------- HEADER ----------------
# st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='title'>📝 Create your AURA account</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Multi-Agent AI Platform Access</div>", unsafe_allow_html=True)

# =========================
# SEND OTP
# =========================
if not st.session_state.otp_sent:

    email = st.text_input("📧 Email address")

    if st.button("📨 Send OTP", use_container_width=True):
        with st.spinner("Sending verification code..."):
            r = requests.post(
                "http://127.0.0.1:8000/auth/send-otp",
                data={"email": email},
                timeout=30
            )

        if r.status_code == 200:
            st.success("✅ OTP sent to your email")
            st.session_state.reg_email = email
            st.session_state.otp_sent = True
            st.rerun()
        else:
            st.error(r.text)

# =========================
# VERIFY OTP
# =========================
else:
    st.info(f"📨 OTP sent to: {st.session_state.reg_email}")

    otp = st.text_input("🔐 OTP code")
    user = st.text_input("👤 Username")
    pwd = st.text_input("🔑 Password", type="password")

    if st.button("✅ Verify & Create Account", use_container_width=True):
        with st.spinner("Creating your account..."):
            r = requests.post(
                "http://127.0.0.1:8000/auth/verify-otp",
                data={
                    "email": st.session_state.reg_email,
                    "otp": otp,
                    "username": user,
                    "password": pwd
                },
                timeout=30
            )

        if r.status_code == 200:
            st.success("🎉 Account created successfully. Please login.")
            del st.session_state.reg_email
            st.session_state.otp_sent = False
            st.switch_page("pages/login.py")
        else:
            st.error("❌ Invalid OTP or expired code")

st.markdown("</div>", unsafe_allow_html=True)
