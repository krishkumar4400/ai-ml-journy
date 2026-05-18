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
You are a strict critic.
""",
        ),
        (
            "human",
            """
REVIEW THIS REPORT:

{report}
""",
        ),
    ]
)

chain = prompt | llm | StrOutputParser()


async def run_critic_agent(report: str):

    return chain.invoke({"report": report})
