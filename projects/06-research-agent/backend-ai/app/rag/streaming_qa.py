import json

from app.services.llm_service import (
    get_llm,
)

from app.rag.retriever import (
    get_retriever,
)

from langchain_core.prompts import (
    ChatPromptTemplate,
)

# -----------------------------------
# LLM
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
Answer ONLY from context.
""",
        ),
        (
            "human",
            """
CONTEXT:
{context}

QUESTION:
{question}
""",
        ),
    ]
)

# -----------------------------------
# Stream Function
# -----------------------------------


async def stream_pdf_answer(
    session_id: str,
    question: str,
):

    # -----------------------------------
    # Event: Retrieving
    # -----------------------------------

    yield json.dumps(
        {
            "type": "trace",
            "message": "Retrieving relevant chunks...",
        }
    ) + "\n"

    retriever = get_retriever()

    docs = retriever.invoke(question)

    # -----------------------------------
    # Event: Context
    # -----------------------------------

    yield json.dumps(
        {
            "type": "trace",
            "message": f"Retrieved {len(docs)} chunks",
        }
    ) + "\n"

    context = "\n\n".join([doc.page_content for doc in docs])

    # -----------------------------------
    # Event: Generation
    # -----------------------------------

    yield json.dumps(
        {
            "type": "trace",
            "message": "Generating AI answer...",
        }
    ) + "\n"

    chain = prompt | llm

    async for chunk in chain.astream(
        {
            "context": context,
            "question": question,
        }
    ):

        yield json.dumps(
            {
                "type": "token",
                "content": chunk.content,
            }
        ) + "\n"

    # -----------------------------------
    # Event: Complete
    # -----------------------------------

    yield json.dumps(
        {
            "type": "trace",
            "message": "Answer complete",
        }
    ) + "\n"
