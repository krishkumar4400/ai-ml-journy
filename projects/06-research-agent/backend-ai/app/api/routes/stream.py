from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from pydantic import BaseModel

from app.services.streaming_service import (
    stream_research_report,
)

router = APIRouter()

# -----------------------------------
# Request Model
# -----------------------------------


class StreamRequest(BaseModel):
    topic: str


# -----------------------------------
# Streaming Endpoint
# -----------------------------------


@router.post("/")
async def stream_research(request: StreamRequest):

    generator = stream_research_report(request.topic)

    return StreamingResponse(
        generator,
        media_type="text/plain",
    )
