import requests

from bs4 import BeautifulSoup

from langchain.tools import tool

# -----------------------------------
# Scraper Tool
# -----------------------------------


@tool
def scrape_website(url: str) -> str:
    """
    Scrape website content.
    """

    try:

        headers = {"User-Agent": "Mozilla/5.0"}

        response = requests.get(
            url,
            headers=headers,
            timeout=10,
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser",
        )

        paragraphs = soup.find_all("p")

        text = "\n".join(p.get_text(strip=True) for p in paragraphs[:30])

        return text[:5000]

    except Exception as e:

        return f"""
Failed to scrape:
{url}

Error:
{str(e)}
"""
