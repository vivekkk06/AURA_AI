from tools.groq_llm import groq_chat

def researcher(info):
    return groq_chat([
        {"role": "system", "content": "You research and summarize."},
        {"role": "user", "content": info}
    ])
