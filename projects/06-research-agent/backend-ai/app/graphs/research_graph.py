from typing import TypedDict

# -----------------------------------
# Graph State
# -----------------------------------
from langgraph.graph import (
    StateGraph,
    END,
)

from app.agents.search_agent import (
    run_search_agent,
)

from app.agents.writer_agent import (
    run_writer_agent,
)

from app.agents.critic_agent import (
    run_critic_agent,
)


class ResearchState(TypedDict):

    topic: str

    research: str

    report: str

    feedback: str

    rewrite: bool

# -----------------------------------
# Search Node
# -----------------------------------


async def search_node(state: ResearchState):

    research = await run_search_agent(state["topic"])

    return {"research": research}


# -----------------------------------
# Writer Node
# -----------------------------------


async def writer_node(state: ResearchState):

    report = await run_writer_agent(
        topic=state["topic"],
        research=state["research"],
    )

    return {"report": report}


# -----------------------------------
# Critic Node
# -----------------------------------


async def critic_node(state: ResearchState):

    feedback = await run_critic_agent(state["report"])

    rewrite = False

    if "weakness" in feedback.lower():
        rewrite = True

    return {
        "feedback": feedback,
        "rewrite": rewrite,
    }

# -----------------------------------
# Conditional Edge
# -----------------------------------


def should_rewrite(state: ResearchState):

    if state["rewrite"]:
        return "writer"

    return END

# -----------------------------------
# Build Graph
# -----------------------------------

graph = StateGraph(ResearchState)

# -----------------------------------
# Add Nodes
# -----------------------------------

graph.add_node(
    "search",
    search_node,
)

graph.add_node(
    "writer",
    writer_node,
)

graph.add_node(
    "critic",
    critic_node,
)

# -----------------------------------
# Entry Point
# -----------------------------------

graph.set_entry_point("search")

# -----------------------------------
# Edges
# -----------------------------------

graph.add_edge(
    "search",
    "writer",
)

graph.add_edge(
    "writer",
    "critic",
)

# -----------------------------------
# Conditional Edge
# -----------------------------------

graph.add_conditional_edges(
    "critic",
    should_rewrite,
)

# -----------------------------------
# Compile
# -----------------------------------

research_graph = graph.compile()
