# app/models/consultation.py
from pydantic import BaseModel

class ConsultationInput(BaseModel):
    language: str
    symptoms: str
    age: int = None
    gender: str = None
