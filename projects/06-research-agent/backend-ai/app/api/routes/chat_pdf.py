from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.qa_chain import (
    ask_pdf_question,
)

router = APIRouter()

# -----------------------------------
# Request Model
# -----------------------------------


class ChatRequest(BaseModel):

    session_id: str
    question: str


# -----------------------------------
# Chat Endpoint
# -----------------------------------


@router.post("/")
async def chat_with_pdf(request: ChatRequest):

    result = await ask_pdf_question(
        session_id=request.session_id,
        question=request.question,
    )

    return {
        "success": True,
        "data": result,
    }
