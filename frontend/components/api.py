import requests
import streamlit as st

BASE = "http://127.0.0.1:8000"


def get_headers(json_mode=False):
    headers = {}
    token = st.session_state.get("token")

    if token:
        headers["Authorization"] = f"Bearer {token}"

    if json_mode:
        headers["Content-Type"] = "application/json"

    return headers


# ---------- NORMAL POST (forms / uploads) ----------
def api_post(path, data=None, files=None):
    return requests.post(
        BASE + path,
        data=data,
        files=files,
        headers=get_headers(),
        timeout=1800
    )


# ---------- JSON POST ----------
def api_post_json(path, payload: dict):
    return requests.post(
        BASE + path,
        json=payload,
        headers=get_headers(json_mode=True),
        timeout=1800
    )


# ---------- GET ----------
def api_get(path):
    return requests.get(
        BASE + path,
        headers=get_headers(),
        timeout=60
    )
