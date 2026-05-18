# from langchain_ollama import ChatOllama

# # -----------------------------------
# # LLM
# # -----------------------------------

# llm = ChatOllama(
#     model="gemma:7b",
#     temperature=0,
# )

# # -----------------------------------
# # Getter
# # -----------------------------------


# def get_llm():

#     return llm

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="phi3:mini",
    temperature=0,
)


def get_llm():
    return llm
