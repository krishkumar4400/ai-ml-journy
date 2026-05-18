import re

# -----------------------------------
# Extract URLs
# -----------------------------------


def extract_urls(text: str):

    urls = re.findall(
        r"https?://[^\s]+",
        text,
    )

    return list(set(urls))
