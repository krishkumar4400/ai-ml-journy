from fastapi import APIRouter

router = APIRouter()

# -----------------------------------
# Health Check
# -----------------------------------


@router.get("/")
async def health_check():

    return {
        "status": "healthy",
        "service": "AI Research Backend",
    }
