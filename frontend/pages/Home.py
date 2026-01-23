import streamlit as st
from components.ui import load_css

load_css()

st.markdown("""
<div style="text-align:center; padding-top:40px;">
    <h1>🧠 MULTI USER AI</h1>
    <h3>Multi-Agent • Persistent Memory • Resume AI • Document QA</h3>
    <p style="color:#94a3b8;">Your personal AI operating system</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- CARDS ----------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("### 💬 Chat AI")
    st.write("Smart multi-agent reasoning system.")
    st.page_link("pages/chat_ai.py", label="➡ Open Chat AI")

with c2:
    st.markdown("### 📄 Resume AI")
    st.write("AI interview & skill analysis.")
    st.page_link("pages/Resume_AI.py", label="➡ Open Resume AI")

with c3:
    st.markdown("### 📚 Document AI")
    st.write("Chat with PDFs & notes.")
    st.page_link("pages/Document_QA.py", label="➡ Open Document AI")

with c4:
    st.markdown("### 🧠 Memory AI")
    st.write("Your AI remembers everything.")
    st.page_link("pages/Memory_Dashboard.py", label="➡ Open Memory Dashboard")

st.divider()
st.info("👉 Use the sidebar to start.")
