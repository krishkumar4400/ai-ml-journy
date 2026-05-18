from fastapi import APIRouter
from pydantic import BaseModel

from app.services.research_service import (
    generate_research_report,
)

router = APIRouter()

# -----------------------------------
# Request Model
# -----------------------------------


class ResearchRequest(BaseModel):
    topic: str


# -----------------------------------
# Research Endpoint
# -----------------------------------


@router.post("/")
async def research_endpoint(request: ResearchRequest):

    result = await generate_research_report(request.topic)

    return {
        "success": True,
        "data": result,
    }
