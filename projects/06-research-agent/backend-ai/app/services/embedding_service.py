from langchain_ollama import (
    OllamaEmbeddings,
)

embeddings = OllamaEmbeddings(model="nomic-embed-text")


def get_embeddings():
    return embeddings
