# app/services/gpt_health.py
import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def get_health_response(user_input: str) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "You are BUA, a multilingual AI assistant providing respectful, accurate, and youth-friendly sexual and reproductive health information. "
                "You DO NOT diagnose medical conditions. Instead, you give culturally sensitive guidance in simple language. "
                "If a question is unclear or too serious, suggest visiting a local clinic."
            )
        },
        {
            "role": "user",
            "content": user_input
        }
    ]

    response = await client.chat.completions.create(
        model="gpt-4.1-mini-2025-04-14",  # GPT-4.1 mini
        messages=messages,
        temperature=0.5
    )

    return response.choices[0].message.content.strip()
