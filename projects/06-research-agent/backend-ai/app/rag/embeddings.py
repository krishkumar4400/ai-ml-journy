from langchain_ollama import OllamaEmbeddings

# -----------------------------------
# Embedding Model
# -----------------------------------

embeddings = OllamaEmbeddings(model="nomic-embed-text")

# -----------------------------------
# Getter
# -----------------------------------


def get_embeddings():

    return embeddings
