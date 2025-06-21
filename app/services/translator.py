# app/services/translator.py
from openai import AsyncOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def translate_text(text: str, source_lang: str, target_lang: str) -> str:
    prompt = (
    f"You are a multilingual translator. Translate the following from {source_lang} to {target_lang}. "
    "Sipitori is a South African township dialect with a mix of Setswana, Sepedi, Zulu, and English. "
    "Preserve the cultural tone but translate clearly and respectfully.\n\n"
    f"\"{text}\""
      )


    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a multilingual translator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()
