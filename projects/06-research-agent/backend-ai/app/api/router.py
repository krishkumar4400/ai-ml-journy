from fastapi import APIRouter

from app.api.routes.health import router as health_router
from app.api.routes.research import router as research_router
from app.api.routes.stream import (
    router as stream_router,
)
from app.api.routes.upload import (
    router as upload_router,
)
from app.api.routes.chat_pdf import (
    router as chat_pdf_router,
)
from app.api.routes.langgraph import (
    router as langgraph_router,
)
from app.api.routes.chat_pdf_stream import (
    router as chat_pdf_stream_router,
)
# from app.api.routes.multi_agent import (
#     router as multi_agent_router,
# )
from app.api.routes.multi_agent_stream import (
    router as multi_agent_stream_router,
)

# -----------------------------------
# Main API Router
# -----------------------------------

api_router = APIRouter()

# -----------------------------------
# Register Routes
# -----------------------------------

api_router.include_router(
    health_router,
    prefix="/health",
    tags=["Health"],
)

api_router.include_router(
    research_router,
    prefix="/research",
    tags=["Research"],
)

api_router.include_router(
    stream_router,
    prefix="/stream",
    tags=["Streaming"],
)

api_router.include_router(
    upload_router,
    prefix="/upload",
    tags=["Upload"],
)
api_router.include_router(
    chat_pdf_router,
    prefix="/chat-pdf",
    tags=["Chat PDF"],
)
api_router.include_router(
    langgraph_router,
    prefix="/langgraph",
    tags=["LangGraph"],
)
api_router.include_router(
    chat_pdf_stream_router,
    prefix="/chat-pdf-stream",
    tags=["Chat PDF Stream"],
)
# api_router.include_router(
#     multi_agent_router,
#     prefix="/multi-agent",
#     tags=["Multi Agent"],
# )
api_router.include_router(
    multi_agent_stream_router,
    prefix="/multi-agent-stream",
    tags=["Multi-Agent Stream"],
)
