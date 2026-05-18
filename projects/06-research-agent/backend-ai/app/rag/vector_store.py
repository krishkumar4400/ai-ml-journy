from langchain_chroma import Chroma

from app.rag.embeddings import (
    get_embeddings,
)

# -----------------------------------
# Create Vector DB
# -----------------------------------


def create_vector_store(
    chunks,
):

    if not chunks:
        raise ValueError("No chunks provided.")

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory="./chroma_db",
    )

    return vector_store


# from langchain_chroma import Chroma

# from app.services.embedding_service import (
#     get_embeddings,
# )

# vector_store = Chroma(
#     collection_name="pdf_collection",
#     embedding_function=get_embeddings(),
#     persist_directory="./chroma_db",
# )


# def get_vector_store():
#     return vector_store
