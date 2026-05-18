from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from app.services.llm_service import get_llm
from app.agents.orchestrator import (
    run_research_workflow,
)

# -----------------------------------
# Load LLM
# -----------------------------------

llm = get_llm()

# -----------------------------------
# Writer Prompt
# -----------------------------------

writer_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert AI research writer.

Write professional,
clear,
detailed research reports.
""",
        ),
        (
            "human",
            """
Generate a detailed research report on:

TOPIC:
{topic}

Structure:
1. Introduction
2. Key Trends
3. Future Predictions
4. Challenges
5. Conclusion

Be factual and detailed.
""",
        ),
    ]
)

# -----------------------------------
# Chain
# -----------------------------------

writer_chain = writer_prompt | llm | StrOutputParser()

# -----------------------------------
# Service Function
# -----------------------------------


# -----------------------------------
# Service
# -----------------------------------


async def generate_research_report(topic: str):

    result = await run_research_workflow(topic)

    return result
