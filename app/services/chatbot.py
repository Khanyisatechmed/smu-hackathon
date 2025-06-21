# app/services/chatbot.py
from app.services.gpt_health import get_health_response
from app.services.translator import translate_text


async def handle_chatbot_query(text: str, source_lang: str, target_lang: str) -> str:
    # Translate to English (only if needed)
    english_input = await translate_text(text, source_lang, "en") if source_lang != "en" else text

    # Generate health-safe response
    english_response = await get_health_response(english_input)

    # Translate back to target language (if needed)
    final_output = await translate_text(english_response, "en", target_lang) if target_lang != "en" else english_response

    return final_output
