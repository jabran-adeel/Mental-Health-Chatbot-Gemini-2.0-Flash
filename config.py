import openai
from dotenv import load_dotenv
import os

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_health_bot(question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful and safe health assistant. Do NOT give prescriptions or serious medical advice. Keep answers general and friendly."
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0.5,
        max_tokens=150
    )
    return response.choices[0].message.content