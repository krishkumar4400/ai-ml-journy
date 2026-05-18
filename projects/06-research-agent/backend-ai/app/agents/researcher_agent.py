from app.tools.web_search import (
    tavily_search,
)

# -----------------------------------
# Research Agent
# -----------------------------------


async def run_researcher_agent(
    topic: str,
):

    results = tavily_search(topic)

    return results
