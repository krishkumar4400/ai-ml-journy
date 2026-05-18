from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from app.services.llm_service import get_llm

# -----------------------------------
# Load LLM
# -----------------------------------

llm = get_llm()

# -----------------------------------
# Prompt
# -----------------------------------

critic_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a strict research critic.
""",
        ),
        (
            "human",
            """
Review this report.

REPORT:
{report}

Provide:
- score out of 10
- strengths
- weaknesses
- suggestions
""",
        ),
    ]
)

# -----------------------------------
# Chain
# -----------------------------------

critic_chain = critic_prompt | llm | StrOutputParser()
