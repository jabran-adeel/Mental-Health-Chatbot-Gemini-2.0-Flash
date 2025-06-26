# 🧠 Mental Health Chatbot – Gemini API (Task 5)

A simple and secure mental health chatbot powered by **Google Gemini 2.0 Flash**. It gives supportive, general responses to user input without offering diagnosis, therapy, or medical advice.

---

## ✨ Features

- 🤖 Built using Google Gemini 2.0 Flash
- 🔒 Uses `.env` to hide API key
- 💬 Prompt-engineered for safe, empathetic replies
- ⚙️ Clean Python structure (main/config/requirements)

---

## 📁 Project Structure

mental_health_chatbot/

├── main.py  CLI chatbot

├── config.py  Gemini request logic

├── .env  Gemini API key (not pushed)

├── .gitignore  Ignore secrets & venv

├── requirements.txt

└── README.md


---

## 🚀 How to Run

### 1. Clone this Repo
```bash
git clone https://github.com/jabran-adeel/mental_health_chatbot.git
cd mental_health_chatbot
```
### 2. Create .env File with API Key
```bash
GEMINI_API_KEY=AIzaSyXXXX...your_key_here
```
### 3. Create and Activate a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate     # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```
### 4. Install Dependencies
```bash
pip install -r requirements.txt
```
### 5. Run the Bot
```bash
python main.py
```
🗨️ Try questions like:

`"I'm feeling anxious lately."`

`"I can't sleep. What should I do?"`

`"I'm overwhelmed with work stress."`

### 🛠 Tech Stack
~ Python 3

~ Google Gemini API (gemini-2.0-flash)

~ python-dotenv

~ requests

### ⚠️ Disclaimer
This chatbot is for informational and educational use only. It does not provide therapy, diagnosis, or medical recommendations. Please consult a professional for medical or mental health concerns.

### 🙋‍♂️ Created by `Jabran Adeel`
This project is part of my AI/ML Internship Series.
⭐ Star the repo if you found it useful!
