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


def api_post(path, data=None, files=None):
    return requests.post(
        BASE + path,
        data=data,
        files=files,
        headers=get_headers(),
        timeout=600
    )


def api_post_json(path, payload: dict):
    return requests.post(
        BASE + path,
        json=payload,                     # ✅ must use json=
        headers=get_headers(json_mode=True),  # ✅ forces JSON parsing in FastAPI
        timeout=600
    )


def api_get(path):
    return requests.get(
        BASE + path,
        headers=get_headers(),
        timeout=60
    )
