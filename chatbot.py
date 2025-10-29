import os
import json
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

# load HF_TOKEN from .env
load_dotenv()  

# Initialize HF client 
client = InferenceClient(
    model="meta-llama/Llama-3.1-8B-Instruct",
    token=os.getenv("HF_TOKEN")
)

history_file = "chat_history.json"

# Load and save chat memory
def load_history():
    if os.path.exists(history_file):
        with open(history_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return [{"role": "system", "content": "You are Jarvis, a helpful assistant."}]

def save_history(history):
    with open(history_file, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

# Chat logic
def chat(message: str, history: list) -> str:
    history.append({"role": "user", "content": message})

    messages = [{"role": h["role"], "content": h["content"]} for h in history]

    response = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=messages,
        max_tokens=512
    )

    reply = response.choices[0].message["content"]
    history.append({"role": "assistant", "content": reply})
    save_history(history)
    return reply

# Run chatbot
if __name__ == "__main__":
    print("Jarvis ready with persistent memory! Type 'exit' to quit.\n")
    history = load_history()

    while True:
        msg = input("You: ")
        if msg.lower() == "exit":
            print("Saving chat history... Bye!")
            save_history(history)
            break
        print("Jarvis:", chat(msg, history))
