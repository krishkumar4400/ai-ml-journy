from langchain_core.prompts import ChatPromptTemplate

from app.services.llm_service import (
    get_llm,
)

# -----------------------------------
# Load LLM
# -----------------------------------

llm = get_llm()

# -----------------------------------
# Prompt
# -----------------------------------

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert AI researcher.
""",
        ),
        (
            "human",
            """
Generate a detailed report about:

TOPIC:
{topic}
""",
        ),
    ]
)

# -----------------------------------
# Streaming Generator
# -----------------------------------


async def stream_research_report(topic: str):

    chain = prompt | llm

    async for chunk in chain.astream({"topic": topic}):

        if chunk.content:

            yield chunk.content
