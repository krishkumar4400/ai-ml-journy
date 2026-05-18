from fastapi import APIRouter

from fastapi.responses import StreamingResponse

import asyncio

router = APIRouter()


async def fake_ai_stream(prompt: str):

    words = (f"AI response for: {prompt}").split()

    for word in words:

        yield word + " "

        await asyncio.sleep(0.1)


@router.post("/stream")
async def stream_chat(body: dict):

    prompt = body.get("message", "")

    return StreamingResponse(fake_ai_stream(prompt), media_type="text/plain")
