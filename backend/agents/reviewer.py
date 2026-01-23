from tools.groq_llm import groq_chat

def reviewer(output):
    return groq_chat([
        {"role": "system", "content": "You review and improve answers."},
        {"role": "user", "content": output}
    ])
