# app/services/ai_agent.py
import whisper
import os

model = whisper.load_model("base")  # You can also use "tiny", "small", "medium", or "large"

def transcribe_audio(audio_path: str) -> str:
    result = model.transcribe(audio_path)
    return result["text"]
