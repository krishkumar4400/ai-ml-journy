from app.tools.web_search import (
    tavily_search,
)

# -----------------------------------
# Search Agent
# -----------------------------------


async def run_search_agent(topic: str):

    result = tavily_search.invoke({"query": topic})

    return result
