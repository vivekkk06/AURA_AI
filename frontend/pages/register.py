import streamlit as st
import requests
from components.ui import load_css

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Register | MULTI USER AI",
    page_icon="📝",
    layout="centered"
)

load_css()

# ------------------ GLOBAL CARD STYLE ------------------
st.markdown("""
<style>
.auth-card {
    background: radial-gradient(circle at top left, #0f172a, #020617);
    padding: 36px;
    border-radius: 24px;
    border: 1px solid rgba(148,163,184,0.15);
    box-shadow: 0 0 45px rgba(56,189,248,0.10);
    max-width: 480px;
    margin: auto;
}
.auth-title {
    font-size: 36px;
    font-weight: 800;
    text-align: center;
}
.auth-sub {
    color: #94a3b8;
    text-align: center;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ SESSION ------------------
if "otp_sent" not in st.session_state:
    st.session_state.otp_sent = False

# ------------------ CARD START ------------------
# st.markdown("<div class='auth-card'>", unsafe_allow_html=True)

st.markdown("<div class='auth-title'>📝 Create your account</div>", unsafe_allow_html=True)
st.markdown("<div class='auth-sub'>Access the Multi-Agent AI Platform</div>", unsafe_allow_html=True)

st.divider()

# =========================
# SEND OTP
# =========================
if not st.session_state.otp_sent:

    email = st.text_input("📧 Email address")

    if st.button("📨 Send OTP", use_container_width=True):
        if not email:
            st.warning("Please enter your email")
            st.stop()

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
        if not otp or not user or not pwd:
            st.warning("Please fill all fields")
            st.stop()

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
