from langchain_core.prompts import (
    ChatPromptTemplate,
)

from langchain_core.output_parsers import (
    StrOutputParser,
)

from app.services.llm_service import (
    get_llm,
)

llm = get_llm()

# -----------------------------------
# Prompt
# -----------------------------------

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a planning agent.

Break complex research tasks
into clear research objectives.
""",
        ),
        (
            "human",
            """
TOPIC:
{topic}
""",
        ),
    ]
)

chain = prompt | llm | StrOutputParser()

# -----------------------------------
# Main Function
# -----------------------------------


async def run_planner_agent(topic: str):

    return chain.invoke({"topic": topic})
