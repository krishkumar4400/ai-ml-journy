from collections import defaultdict

# -----------------------------------
# In-Memory Chat Store
# -----------------------------------

chat_store = defaultdict(list)

# -----------------------------------
# Add Message
# -----------------------------------


def add_message(
    session_id: str,
    role: str,
    content: str,
):

    chat_store[session_id].append(
        {
            "role": role,
            "content": content,
        }
    )


# -----------------------------------
# Get Messages
# -----------------------------------


def get_messages(
    session_id: str,
):

    return chat_store[session_id]


# -----------------------------------
# Clear Memory
# -----------------------------------


def clear_memory(
    session_id: str,
):

    chat_store[session_id] = []
