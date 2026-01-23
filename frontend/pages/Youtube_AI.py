import streamlit as st
from components.api import api_post_json
from components.ui import load_css

st.set_page_config("YouTube AI | AURA", layout="wide")
load_css()

# ---------- AUTH ----------
if "token" not in st.session_state:
    st.error("🔐 Please login first")
    st.stop()

# ---------- HEADER ----------
st.markdown("""
<div style="text-align:center;">
    <h1>🎥 YouTube Intelligence</h1>
    <h4>AI-powered video understanding & summarization</h4>
</div>
""", unsafe_allow_html=True)

st.divider()

# ---------- INPUT ----------
url = st.text_input(
    "📎 Paste YouTube video link",
    placeholder="https://www.youtube.com/watch?v=..."
)

if st.button("🚀 Generate AI Summary", use_container_width=True):

    if not url:
        st.warning("Please paste a YouTube link")
        st.stop()

    with st.spinner("🎥 Extracting transcript & thinking..."):
        r = api_post_json("/youtube/summarize", {"url": url})

    if r.status_code != 200:
        st.error(r.text)
        st.stop()

    st.session_state.yt = r.json()

# ---------- OUTPUT ----------
if "yt" in st.session_state:

    data = st.session_state.yt

    st.divider()
    st.subheader("🧠 AI Video Summary")

    with st.container(border=True):
        st.markdown(data["summary"])

    with st.expander("📜 Transcript Preview"):
        st.write(data["transcript_preview"])

    st.success("✅ Video analyzed successfully")
