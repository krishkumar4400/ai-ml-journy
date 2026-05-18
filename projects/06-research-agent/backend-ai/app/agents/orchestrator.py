from app.agents.search_agent import (
    run_search_agent,
)

from app.agents.writer_agent import (
    run_writer_agent,
)

from app.agents.critic_agent import (
    run_critic_agent,
)

from app.tools.url_extractor import (
    extract_urls,
)

from app.tools.scraper import (
    scrape_website,
)

# -----------------------------------
# Main Workflow
# -----------------------------------


async def run_research_workflow(topic: str):

    # -----------------------------------
    # STEP 1 - SEARCH
    # -----------------------------------

    search_results = await run_search_agent(topic)

    # -----------------------------------
    # STEP 2 - EXTRACT URLS
    # -----------------------------------

    urls = extract_urls(search_results)

    # -----------------------------------
    # STEP 3 - SCRAPE URLS
    # -----------------------------------

    scraped_content = []

    for url in urls[:3]:

        content = scrape_website.invoke({"url": url})

        scraped_content.append(f"""
SOURCE:
{url}

CONTENT:
{content}
""")

    combined_research = f"""
SEARCH RESULTS:
{search_results}

SCRAPED CONTENT:
{' '.join(scraped_content)}
"""

    # -----------------------------------
    # STEP 4 - WRITER
    # -----------------------------------

    report = await run_writer_agent(
        topic,
        combined_research,
    )

    # -----------------------------------
    # STEP 5 - CRITIC
    # -----------------------------------

    feedback = await run_critic_agent(report)

    # -----------------------------------
    # FINAL RESPONSE
    # -----------------------------------

    return {
        "topic": topic,
        "sources": urls,
        "report": report,
        "feedback": feedback,
    }
