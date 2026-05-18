import json

from app.agents.planner_agent import (
    run_planner_agent,
)

from app.agents.researcher_agent import (
    run_researcher_agent,
)

from app.agents.writer_agent import (
    run_writer_agent,
)

from app.agents.critic_agent import (
    run_critic_agent,
)

# -----------------------------------
# Streaming Multi-Agent Workflow
# -----------------------------------


async def stream_agent_team(topic: str):

    # -----------------------------------
    # Planner
    # -----------------------------------

    yield json.dumps(
        {
            "type": "status",
            "agent": "Planner Agent",
            "message": "Planning research strategy...",
        }
    ) + "\n"

    plan = await run_planner_agent(topic)

    yield json.dumps(
        {
            "type": "agent",
            "agent": "Planner Agent",
            "output": plan,
        }
    ) + "\n"

    # -----------------------------------
    # Researcher
    # -----------------------------------

    yield json.dumps(
        {
            "type": "status",
            "agent": "Research Agent",
            "message": "Searching web...",
        }
    ) + "\n"

    research = await run_researcher_agent(topic)

    yield json.dumps(
        {
            "type": "agent",
            "agent": "Research Agent",
            "output": research,
        }
    ) + "\n"

    # -----------------------------------
    # Writer
    # -----------------------------------

    yield json.dumps(
        {
            "type": "status",
            "agent": "Writer Agent",
            "message": "Writing report...",
        }
    ) + "\n"

    report = await run_writer_agent(
        plan=plan,
        research=research,
    )

    yield json.dumps(
        {
            "type": "agent",
            "agent": "Writer Agent",
            "output": report,
        }
    ) + "\n"

    # -----------------------------------
    # Critic
    # -----------------------------------

    yield json.dumps(
        {
            "type": "status",
            "agent": "Critic Agent",
            "message": "Reviewing report...",
        }
    ) + "\n"

    feedback = await run_critic_agent(report)

    yield json.dumps(
        {
            "type": "agent",
            "agent": "Critic Agent",
            "output": feedback,
        }
    ) + "\n"
