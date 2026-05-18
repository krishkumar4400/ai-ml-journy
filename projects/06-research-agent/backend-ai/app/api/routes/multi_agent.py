from fastapi import APIRouter

from pydantic import BaseModel

from app.multi_agents.team import (
    run_agent_team,
)

router = APIRouter()

# -----------------------------------
# Request
# -----------------------------------


class TeamRequest(BaseModel):

    topic: str


# -----------------------------------
# Endpoint
# -----------------------------------


@router.post("/")
async def multi_agent_route(request: TeamRequest):

    result = await run_agent_team(request.topic)

    return {
        "success": True,
        "data": result,
    }
