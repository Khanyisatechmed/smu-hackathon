# app/api/v1/endpoints/consultation.py

from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from app.services.ai_agent import transcribe_audio           # Whisper speech-to-text
from app.services.translator import translate_text
from app.services.tts import text_to_speech                  # gTTS text-to-speech
from app.services.chatbot import handle_chatbot_query
from fastapi.staticfiles import StaticFiles
import os

router = APIRouter()

# 🎹 Audio to Text (STT)
@router.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"
    if "../" in file_path or "..\\" in file_path:
        raise Exception("Invalid file path")
    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = transcribe_audio(file_path)
    os.remove(file_path)
    return {"transcription": text}

# 🧠 Multilingual Chatbot: Text in → GPT → Voice out
@router.post("/speak")
async def speak(
    text: str,
    lang: str = "en",                     # TTS voice output language
    source_lang: str = "sipitori",        # Input language
    target_lang: str = "sipitori",        # Output response language
    include_text: bool = True,
    translate_to_setswana: bool = False
):
    response_text = await handle_chatbot_query(text, source_lang, target_lang)

    setswana_version = None
    if translate_to_setswana:
        from app.services.translator import translate_text
        setswana_version = await translate_text(response_text, target_lang, "ts")

    audio_path = text_to_speech(response_text, lang)

    return JSONResponse({
        "text_response": response_text if include_text else None,
        "setswana_translation": setswana_version,
        "audio_file": f"/static/{os.path.basename(audio_path)}"
    })
