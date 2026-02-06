import streamlit as st
import requests
from components.ui import load_css
# ---------------- CONFIG ----------------
st.set_page_config("Login | AURA AI", layout="centered")


load_css()
# ---------------- GLOBAL STYLE ----------------
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top left, #0f172a, #020617);
    color: white;
}

.block-container {
    padding-top: 3rem;
    max-width: 420px;
}

.login-card {
    background: rgba(15,23,42,0.85);
    border-radius: 22px;
    padding: 35px;
    border: 1px solid rgba(148,163,184,0.18);
    box-shadow: 0 0 50px rgba(56,189,248,0.12);
}

.login-title {
    text-align: center;
    font-size: 36px;
    font-weight: 800;
}

.login-sub {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 25px;
}

input {
    background: rgba(15,23,42,0.95) !important;
    color: white !important;
    border-radius: 14px !important;
    border: 1px solid rgba(148,163,184,0.3) !important;
}

input:focus {
    border: 1px solid #38bdf8 !important;
    box-shadow: 0 0 12px rgba(56,189,248,0.35) !important;
}

.stButton > button {
    border-radius: 14px;
    height: 48px;
    font-weight: 700;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- CARD START ----------------
# st.markdown("<div class='login-card'>", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<div class='login-title'>🔐 Login to AURA</div>", unsafe_allow_html=True)
st.markdown("<div class='login-sub'>Access your multi-agent AI platform</div>", unsafe_allow_html=True)

st.divider()

# ---------------- FORM ----------------
u = st.text_input("👤 Username")
p = st.text_input("🔑 Password", type="password")

if st.button("🚀 Login", use_container_width=True):
    try:
        r = requests.post(
            "http://127.0.0.1:8000/auth/login",
            data={"username": u, "password": p},
            timeout=30
        )

        if r.status_code == 200:
            st.session_state.token = r.json()["access_token"]

            st.write("TOKEN:", st.session_state.token)
            st.session_state.current_user = u
            st.success("✅ Login successful")
            st.switch_page("app.py")
        else:
            st.error("❌ Invalid username or password")

    except Exception as e:
        st.error("❌ Backend not reachable")
        st.code(str(e))

st.divider()

# ---------------- REGISTER ----------------
st.markdown("### 🆕 New here?")
st.markdown("Create an account to start using the AI platform.")

if st.button("✨ Create new account → Register", use_container_width=True):
    st.switch_page("pages/register.py")

# ---------------- CARD END ----------------
st.markdown("</div>", unsafe_allow_html=True)
