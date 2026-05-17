from langchain.tools import tool
import requests
from bs4 import BeautifulSoup


@tool
def web_search(query: str) -> str:
    """
    Search the web for information.
    """

    url = f"https://duckduckgo.com/html/?q={query}"

    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return "Search failed."

    soup = BeautifulSoup(response.text, "html.parser")

    results = []

    for a in soup.select(".result__a")[:5]:
        title = a.get_text(strip=True)
        link = a.get("href")

        results.append(f"{title}\n{link}")

    return "\n\n".join(results)


@tool
def scrape_url(url: str) -> str:
    """
    Scrape content from a URL.
    """

    try:
        headers = {"User-Agent": "Mozilla/5.0"}

        response = requests.get(url, headers=headers, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")

        text = "\n".join(p.get_text(strip=True) for p in paragraphs[:20])

        return text[:4000]

    except Exception as e:
        return f"Scraping failed: {str(e)}"
