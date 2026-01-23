import streamlit as st
from components.ui import load_css
from components.api import api_get, api_post_json

# ---------------- CONFIG ----------------
st.set_page_config("AURA Memory Dashboard", layout="wide")
load_css()

# ---------------- AUTH CHECK ----------------
if "token" not in st.session_state:
    st.error("🔐 Please login first")
    st.stop()

# ---------------- TITLE ----------------
st.title("🧠 AI Memory & Logs Center")
st.caption("Complete activity, memory, and intelligence overview")

# ---------------- FETCH DATA ----------------
res = api_get("/memory/dashboard")

if res.status_code != 200:
    st.error("❌ Backend not connected or session expired")
    st.stop()

data = res.json()

# ---------------- METRICS ----------------
c1, c2, c3 = st.columns(3)

c1.metric("💬 Total Conversations", data.get("total_chats", 0))
c2.metric("🧠 Stored Memories", data.get("total_memories", 0))
c3.metric("📄 Documents Indexed", data.get("total_docs", 0))

st.divider()

# ---------------- RECENT LOGS ----------------
st.subheader("🕒 Recent AI Activity")

recent = data.get("recent_chats", [])

if not recent:
    st.info("No conversations yet.")
else:
    for chat in recent:
        role = "🧑 User" if chat["role"] == "user" else "🤖 AI"
        with st.container(border=True):
            st.markdown(f"**{role}**")
            st.write(chat["content"])

# ---------------- MEMORY SEARCH ----------------
st.divider()
st.subheader("🔍 Search AI Memory")

query = st.text_input("Search anything the AI remembers")

if query:
    r = api_post_json("/memory/search", {"query": query})

    if r.status_code != 200:
        st.error(r.text)
        st.stop()

    results = r.json().get("results", [])

    if not results:
        st.warning("No matching memory found.")
    else:
        for i, mem in enumerate(results, 1):
            st.markdown(f"**{i}.** {mem}")

# ---------------- SYSTEM INFO ----------------
st.divider()
st.subheader("📊 System Logs")

st.markdown("""
✔ User prompts  
✔ AI replies  
✔ Vector embeddings  
✔ Resume interviews  
✔ Document memory  
""")

st.success("✅ Memory system active and running")
