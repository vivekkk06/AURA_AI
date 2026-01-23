import requests, os

GROQ_KEY = os.getenv("GROQ_API_KEY")
URL = "https://api.groq.com/openai/v1/chat/completions"

def groq_chat(messages, model="llama-3.3-70b-versatile"):
    headers = {
        "Authorization": f"Bearer {GROQ_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "model": model,
        "messages": messages,
        "temperature": 0.4
    }
    r = requests.post(URL, json=body, headers=headers)
    return r.json()["choices"][0]["message"]["content"]
