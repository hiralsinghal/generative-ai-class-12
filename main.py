import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("gemini_api")
if not api_key:
    raise RuntimeError("Missing gemini_api in the environment or .env file")

client = genai.Client(api_key=api_key)

model = "gemini-3.8-flash"

chat = client.chats.create(model=model, history=[])

while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    response = chat.send_message(user_input)
    print(f"AI: {response.text}")