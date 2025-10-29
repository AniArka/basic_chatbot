# Persistent Memory Chatbot using Llama 3.1

This is a **command-line chatbot** powered by **Meta’s Llama 3.1 8B Instruct model** through the Hugging Face Inference API.  
It supports **persistent memory**, meaning your entire conversation history is saved locally and restored automatically next time you run it.

---

## 🚀 Features

- 💬 Conversational AI powered by **Llama 3.1**
- 🧠 **Persistent chat memory** stored in `chat_history.json`
- 🔐 Secure token management via **.env**
- ⚙️ Lightweight **Python CLI interface**

---

## 📦 Installation

### 1. Clone this repository
```bash
git clone https://github.com/AniArka/basic_chatbot
cd basic_chatbot
```
### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
venv\Scripts\activate      
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
## Setup Hugging Face API Token

1 Go to https://huggingface.co/settings/tokens

2 Create a read access token.

3 Create a .env file in the project root and add:

```bash
HF_TOKEN=your_huggingface_token_here
```
## Usage

Run the chatbot:

```bash

python chatbot.py
```
### Example session:

```bash
Jarvis ready with persistent memory! Type 'exit' to quit.

You: Hello Jarvis
Jarvis: Hello! How can I assist you today?

You: What’s 2 + 2?
Jarvis: 2 + 2 equals 4.

You: exit
Saving chat history... Bye!
```
When you exit, Jarvis automatically saves your chat history to chat_history.json.
Next time you launch it, the conversation resumes where you left off.

## Project Structure
```bash
basic_chatbot/
│
├── chatbot.py               # Main chatbot script
├── chat_history.json       # Persistent chat memory (auto-created)
├── .env                    # Your Hugging Face API token
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```
## How It Works

1 Memory Management

 - Loads chat history from chat_history.json if available.

 - Saves user and assistant messages after every interaction.

2 Model Communication

 - Uses InferenceClient from huggingface_hub to call Llama 3.1.

 - Sends entire chat history for contextual responses.

3 Persistence

 - Maintains full conversation continuity across runs via local JSON storage.

### Requirements

 - Python 3.11.9

 - Hugging Face account + token

 - Internet connection

## License
This project is open-source under the MIT License.
You’re free to modify, distribute, or use it in your own projects.
