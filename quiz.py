import requests
import random

BOT_TOKEN = "8783017327:AAEx5QH2giw8JbtUAhgYJSLOZOX2iq7xam0"
CHAT_ID = "@daily_quiz_demo_channel123"

questions = [
    {
        "q": "What is 2 + 2?",
        "options": ["2", "3", "4", "5"],
        "ans": 2
    },
    {
        "q": "Capital of India?",
        "options": ["Chennai", "Delhi", "Mumbai", "Kolkata"],
        "ans": 1
    }
]

q = random.choice(questions)

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPoll"

data = {
    "chat_id": CHAT_ID,
    "question": q["q"],
    "options": q["options"],
    "type": "quiz",
    "correct_option_id": q["ans"]
}

requests.post(url, json=data)
