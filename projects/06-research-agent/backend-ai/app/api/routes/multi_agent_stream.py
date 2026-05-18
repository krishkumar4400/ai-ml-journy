from fastapi import APIRouter

from fastapi.responses import (
    StreamingResponse,
)

from pydantic import BaseModel

from app.multi_agents.streaming_team import (
    stream_agent_team,
)

router = APIRouter()

# -----------------------------------
# Request
# -----------------------------------


class TeamRequest(BaseModel):

    topic: str


# -----------------------------------
# Stream Route
# -----------------------------------


@router.post("/")
async def multi_agent_stream(request: TeamRequest):

    return StreamingResponse(
        stream_agent_team(request.topic),
        media_type="text/plain",
    )
