from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from app.services.llm_service import (
    get_llm,
)

from app.rag.retriever import (
    get_retriever,
)

from app.memory.chat_memory import (
    add_message,
    get_messages,
)

# -----------------------------------
# Load LLM
# -----------------------------------

llm = get_llm()

# -----------------------------------
# Prompt
# -----------------------------------

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI assistant.

Answer ONLY from:
1. retrieved context
2. conversation history

If answer is unavailable,
say:
"I could not find the answer."
""",
        ),
        (
            "human",
            """
CHAT HISTORY:
{history}

CONTEXT:
{context}

QUESTION:
{question}
""",
        ),
    ]
)

# -----------------------------------
# Main QA Function
# -----------------------------------


async def ask_pdf_question(
    session_id: str,
    question: str,
):

    # -----------------------------------
    # Retriever
    # -----------------------------------

    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    # -----------------------------------
    # Chat History
    # -----------------------------------

    messages = get_messages(session_id)

    history = "\n".join([f"{m['role']}: {m['content']}" for m in messages])

    # -----------------------------------
    # Chain
    # -----------------------------------

    chain = prompt | llm | StrOutputParser()

    answer = chain.invoke(
        {
            "history": history,
            "context": context,
            "question": question,
        }
    )

    # -----------------------------------
    # Save Memory
    # -----------------------------------

    add_message(
        session_id,
        "user",
        question,
    )

    add_message(
        session_id,
        "assistant",
        answer,
    )

    # -----------------------------------
    # Format Sources
    # -----------------------------------

    sources = []

    for doc in docs:

        sources.append(
            {
                "content": doc.page_content,
                "metadata": doc.metadata,
            }
        )

    # -----------------------------------
    # Return
    # -----------------------------------

    return {
        "question": question,
        "answer": answer,
        "sources": sources,
        "session_id": session_id,
    }
