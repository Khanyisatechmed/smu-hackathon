# app/main.py
from fastapi import FastAPI
from app.api.v1.api_router import router as api_router

app = FastAPI(
    title="BUA Consultation Assistant",
    description="Multilingual AI-powered consultation backend",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")
