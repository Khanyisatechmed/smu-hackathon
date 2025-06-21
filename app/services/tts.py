# app/services/tts.py
from gtts import gTTS
import uuid
import os
def text_to_speech(text: str, lang: str = "en") -> str:
    filename = f"output_{uuid.uuid4().hex[:6]}.mp3"
    filepath = os.path.join("audio_outputs", filename)

    os.makedirs("audio_outputs", exist_ok=True)

    tts = gTTS(text=text, lang=lang)
    tts.save(filepath)

    return filepath
