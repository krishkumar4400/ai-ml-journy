from fastapi import APIRouter
from pydantic import BaseModel

from app.services.langgraph_service import (
    run_langgraph_research,
)

router = APIRouter()

# -----------------------------------
# Request
# -----------------------------------


class GraphRequest(BaseModel):

    topic: str


# -----------------------------------
# Endpoint
# -----------------------------------


@router.post("/")
async def langgraph_endpoint(request: GraphRequest):

    result = await run_langgraph_research(request.topic)

    return {
        "success": True,
        "data": result,
    }
