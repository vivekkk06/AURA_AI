import streamlit as st

def load_css():
    st.markdown("""
    <style>

    /* Main background */
    .stApp {
        background: radial-gradient(circle at top, #0f172a, #020617);
        color: #e5e7eb;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #020617, #020617);
        border-right: 1px solid #1e293b;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        padding: 0.6em 1em;
        border: 1px solid #334155;
        background: linear-gradient(135deg, #2563eb, #7c3aed);
        color: white;
        font-weight: 600;
    }

    .stButton > button:hover {
        transform: scale(1.03);
        background: linear-gradient(135deg, #1d4ed8, #6d28d9);
    }

    /* Inputs */
    input, textarea {
        border-radius: 10px !important;
    }

    /* Cards */
    div[data-testid="stVerticalBlock"] > div:has(h3) {
        background: #020617;
        border: 1px solid #1e293b;
        padding: 15px;
        border-radius: 16px;
        box-shadow: 0 0 20px rgba(59,130,246,0.1);
    }

    </style>
    """, unsafe_allow_html=True)
