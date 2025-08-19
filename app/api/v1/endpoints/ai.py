from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_service import AIService

router = APIRouter()
svc = AIService()

class TextIn(BaseModel):
    text: str

@router.post("/summarize")
def summarize(body: TextIn):
    return {"summary": svc.summarize(body.text)}

@router.post("/analyze")
def analyze(body: TextIn):
    return svc.analyze(body.text)
