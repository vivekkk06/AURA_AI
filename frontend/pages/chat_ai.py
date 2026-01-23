import streamlit as st
from components.api import api_post_json

# ---------------- GLOBAL STYLE ----------------
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top left, #0f172a, #020617);
    color: white;
}

.block-container {
    padding-top: 1.5rem;
    max-width: 1100px;
}

.chat-title {
    font-size: 38px;
    font-weight: 800;
}

.chat-sub {
    color: #94a3b8;
    font-size: 16px;
}

.chat-box {
    background: rgba(15,23,42,0.6);
    border-radius: 20px;
    padding: 20px;
    border: 1px solid rgba(148,163,184,0.15);
    box-shadow: 0 0 35px rgba(56,189,248,0.08);
}

div[data-testid="stChatMessage"] {
    background: transparent;
}

div.stChatInput textarea {
    background: rgba(15,23,42,0.8);
    border-radius: 14px;
    border: 1px solid rgba(148,163,184,0.2);
    color: white;
}

div.stChatInput textarea:focus {
    border: 1px solid #38bdf8;
}

</style>
""", unsafe_allow_html=True)

st.set_page_config("Chat AI", layout="wide")
st.title("💬 Multi-Agent Chat")

# ---------- AUTH ----------
if "token" not in st.session_state:
    st.error("Please login first")
    st.stop()

# ---------- SESSION ----------
if "chat" not in st.session_state:
    st.session_state.chat = []

# ---------- SHOW HISTORY ----------
for m in st.session_state.chat:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# ---------- INPUT ----------
q = st.chat_input("Ask anything...")

if q:
    st.session_state.chat.append({"role": "user", "content": q})
    with st.chat_message("user"):
        st.markdown(q)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            r = api_post_json("/chat", {"message": q})

            if r.status_code == 200:
                ans = r.json().get("reply", "No response")
            else:
                ans = f"❌ {r.status_code}\n{r.text}"

            st.markdown(ans)
            st.session_state.chat.append({"role": "assistant", "content": ans})
