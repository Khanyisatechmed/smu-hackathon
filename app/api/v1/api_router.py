# app/api/v1/api_router.py
from fastapi import APIRouter
from app.api.v1.endpoints import consultation

router = APIRouter()
router.include_router(consultation.router, prefix="/consultation", tags=["Consultation"])
