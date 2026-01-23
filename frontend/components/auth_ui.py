import streamlit as st
from components.api import api_post


def send_otp_ui():
    st.subheader("📧 Register - Email Verification")

    email = st.text_input("Email")

    if st.button("Send OTP"):
        r = api_post("/auth/send-otp", data={"email": email})
        if r.status_code == 200:
            st.success("OTP sent to email")
            st.session_state.tmp_email = email
            st.session_state.page = "verify"
            st.rerun()
        else:
            st.error(r.text)


def verify_otp_ui():
    st.subheader("🔐 Verify OTP & Create Account")

    email = st.session_state.get("tmp_email")

    otp = st.text_input("OTP")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Create Account"):
        r = api_post("/auth/verify-otp", data={
            "email": email,
            "otp": otp,
            "username": username,
            "password": password
        })

        if r.status_code == 200:
            st.success("Account created. Please login.")
            st.session_state.page = "login"
            st.rerun()
        else:
            st.error(r.text)


def login_ui():
    st.subheader("🔑 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        r = api_post("/auth/login", data={
            "username": username,
            "password": password
        })

        if r.status_code == 200:
            data = r.json()
            st.session_state.token = data["access_token"]
            st.session_state.user = data["username"]
            st.success("Login successful")
            st.switch_page("pages/dashboard.py")
        else:
            st.error("Invalid credentials")
