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

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert AI writer.
""",
        ),
        (
            "human",
            """
PLAN:
{plan}

RESEARCH:
{research}

Write a detailed report.
""",
        ),
    ]
)

chain = prompt | llm | StrOutputParser()


async def run_writer_agent(
    plan: str,
    research: str,
):

    return chain.invoke(
        {
            "plan": plan,
            "research": research,
        }
    )
