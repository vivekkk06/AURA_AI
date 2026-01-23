import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config("Agent Hub | MULTI USER AI", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top left, #0f172a, #020617);
    color: white;
}

.block-container {
    padding-top: 2rem;
}

.glass {
    background: rgba(15, 23, 42, 0.65);
    backdrop-filter: blur(14px);
    border-radius: 20px;
    padding: 25px;
    border: 1px solid rgba(148,163,184,0.15);
    box-shadow: 0 0 35px rgba(56,189,248,0.08);
    margin-bottom: 25px;
    transition: 0.3s;
}

.glass:hover {
    box-shadow: 0 0 45px rgba(56,189,248,0.25);
    transform: translateY(-4px);
}

.title {
    font-size: 36px;
    font-weight: 800;
}

.soft {
    color: #94a3b8;
    font-size: 16px;
}

div.stButton > button {
    height: 3em;
    font-size: 16px;
    border-radius: 14px;
    background: linear-gradient(135deg, #2563eb, #38bdf8);
    color: white;
    border: none;
    transition: 0.3s;
}

div.stButton > button:hover {
    transform: scale(1.04);
    box-shadow: 0 0 18px rgba(56,189,248,0.6);
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div style="text-align:center; padding-bottom:20px;">
    <div class="title">🧠 Agent Hub</div>
    <p class="soft">Central AI Control Panel</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ================= ROW 1 =================
c1, c2, c3 = st.columns(3)

with c1:
    # st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown("### 💬 Chat AI")
    st.markdown("<p class='soft'>Multi-agent intelligent conversation system</p>", unsafe_allow_html=True)
    if st.button("Open Chat AI", use_container_width=True):
        st.switch_page("pages/chat_ai.py")
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    # st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown("### 📄 Resume AI")
    st.markdown("<p class='soft'>Resume intelligence & interview engine</p>", unsafe_allow_html=True)
    if st.button("Open Resume AI", use_container_width=True):
        st.switch_page("pages/Resume_AI.py")
    st.markdown('</div>', unsafe_allow_html=True)

with c3:
    # st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown("### 📚 Document Q&A")
    st.markdown("<p class='soft'>Chat with PDFs and documents</p>", unsafe_allow_html=True)
    if st.button("Open Document AI", use_container_width=True):
        st.switch_page("pages/Document_QA.py")
    st.markdown('</div>', unsafe_allow_html=True)

# ================= ROW 2 =================
c4, c5 ,c6= st.columns(3)

with c4:
    # st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown("### 🧩 News Researcher AI")
    st.markdown("<p class='soft'>Multi-agent news research system</p>", unsafe_allow_html=True)
    if st.button("Open News Researcher", use_container_width=True):
        st.switch_page("pages/News_Research.py")
    st.markdown('</div>', unsafe_allow_html=True)

with c5:
    # st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown("### 📊 Memory Dashboard")
    st.markdown("<p class='soft'>AI memory, history & analytics</p>", unsafe_allow_html=True)
    if st.button("Open Memory Dashboard", use_container_width=True):
        st.switch_page("pages/Memory_Dashboard.py")
    st.markdown('</div>', unsafe_allow_html=True)
with c6:
    # st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown("### 🎥 YouTube Intelligence")
    st.markdown("<p class='soft'>AI-powered video understanding & summarization</p>", unsafe_allow_html=True)
    if st.button("Open YouTube AI", use_container_width=True):
        st.switch_page("pages/Youtube_AI.py")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.divider()
st.info("⚡ Agent Hub is the central control panel of your AI ecosystem.")
