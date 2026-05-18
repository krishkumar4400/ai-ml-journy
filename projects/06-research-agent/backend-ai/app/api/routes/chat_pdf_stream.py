from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from pydantic import BaseModel

from app.rag.streaming_qa import (
    stream_pdf_answer,
)

router = APIRouter()

# -----------------------------------
# Request
# -----------------------------------


class ChatRequest(BaseModel):

    session_id: str

    question: str


# -----------------------------------
# Stream Route
# -----------------------------------


@router.post("/")
async def stream_chat_pdf(request: ChatRequest):

    return StreamingResponse(
        stream_pdf_answer(
            session_id=request.session_id,
            question=request.question,
        ),
        media_type="text/plain",
    )
