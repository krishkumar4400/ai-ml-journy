from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router

# -----------------------------------
# FastAPI App
# -----------------------------------

app = FastAPI(
    title="AI Research Backend",
    description="Backend APIs for AI Research Agent System",
    version="1.0.0",
)

# -----------------------------------
# CORS
# -----------------------------------

# -----------------------------------
# CORS
# -----------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------
# Include API Router
# -----------------------------------

app.include_router(api_router)

# -----------------------------------
# Root Route
# -----------------------------------


@app.get("/")
async def root():
    return {"message": "AI Research Backend Running 🚀"}
