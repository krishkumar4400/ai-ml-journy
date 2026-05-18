from app.graphs.research_graph import (
    research_graph,
)

# -----------------------------------
# Run Graph
# -----------------------------------


async def run_langgraph_research(topic: str):

    result = await research_graph.ainvoke(
        {
            "topic": topic,
            "research": "",
            "report": "",
            "feedback": "",
            "rewrite": False,
        }
    )

    return result
