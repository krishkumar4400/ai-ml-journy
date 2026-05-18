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

writer_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a professional research writer.

Write highly detailed,
well-structured,
professional reports.
""",
        ),
        (
            "human",
            """
Write a detailed report.

TOPIC:
{topic}

RESEARCH:
{research}

Structure:
1. Introduction
2. Key Findings
3. Future Trends
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
