import streamlit as st

def init_chat(key="chat"):
    if key not in st.session_state:
        st.session_state[key] = []

def show_chat(key="chat"):
    for msg in st.session_state[key]:
        if msg["role"] == "user":
            st.chat_message("user").write(msg["content"])
        else:
            st.chat_message("assistant").write(msg["content"])

def user_input(prompt="Ask something..."):
    return st.chat_input(prompt)

def add_user_msg(text, key="chat"):
    st.session_state[key].append({"role": "user", "content": text})

def add_ai_msg(text, key="chat"):
    st.session_state[key].append({"role": "assistant", "content": text})
