import requests
import random
import json

# URL da API
url = "http://localhost:8000/api/comment/new"

# Dados para os comentários
emails = ["alice@example.com", "bob@example.com", "charlie@example.com", "eve@example.com"]
comments = [
    "This is a great article!",
    "I found this very helpful.",
    "I disagree with the points made.",
    "Interesting perspective.",
    "Well written!",
    "Needs more detail on the topic.",
    "I learned something new today.",
    "Can you provide more examples?"
]

# Função para enviar comentários
def send_comment(content_id):
    data = {
        "email": random.choice(emails),
        "comment": random.choice(comments),
        "content_id": content_id
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response.status_code, response.json()

# Enviar 50 comentários para diferentes content_id
for i in range(50):
    content_id = random.randint(1, 5)
    status, response = send_comment(content_id)
    print(f"Status: {status}, Response: {response}")
