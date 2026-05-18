from tavily import TavilyClient

from dotenv import load_dotenv

import os

# -----------------------------------
# Load ENV
# -----------------------------------

load_dotenv()

# -----------------------------------
# Tavily Client
# -----------------------------------

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# -----------------------------------
# Tavily Search
# -----------------------------------


def tavily_search(
    query: str,
):

    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=5,
    )

    results = response.get("results", [])

    formatted = ""

    for index, result in enumerate(
        results,
        start=1,
    ):

        formatted += f"""
RESULT {index}

TITLE:
{result.get("title")}

CONTENT:
{result.get("content")}

URL:
{result.get("url")}

-------------------------
"""

    return formatted
