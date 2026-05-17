import logging

from typing import Dict, Any

from agents import (
    build_reader_agent,
    build_search_agent,
    writer_chain,
    critic_chain,
)

# -----------------------------------
# Logging
# -----------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

logger = logging.getLogger(__name__)


def run_research_pipeline(topic: str) -> Dict[str, Any]:

    state: Dict[str, Any] = {}

    try:

        # -----------------------------------
        # STEP 1 - SEARCH
        # -----------------------------------

        logger.info("STEP 1 - SEARCH AGENT")

        search_agent = build_search_agent()

        search_result = search_agent.invoke({"input": topic})

        state["search_results"] = search_result["output"]

        # -----------------------------------
        # STEP 2 - READER
        # -----------------------------------

        logger.info("STEP 2 - READER AGENT")

        reader_agent = build_reader_agent()

        reader_result = reader_agent.invoke({"input": state["search_results"]})

        state["scraped_content"] = reader_result["output"]

        # -----------------------------------
        # STEP 3 - WRITER
        # -----------------------------------

        logger.info("STEP 3 - WRITER")

        research_combined = f"""
SEARCH RESULTS:
{state["search_results"]}

SCRAPED CONTENT:
{state["scraped_content"]}
"""

        report = writer_chain.invoke(
            {
                "topic": topic,
                "research": research_combined,
            }
        )

        state["report"] = report

        # -----------------------------------
        # STEP 4 - CRITIC
        # -----------------------------------

        logger.info("STEP 4 - CRITIC")

        feedback = critic_chain.invoke({"report": state["report"]})

        state["feedback"] = feedback

    except Exception as e:

        logger.error(
            "Pipeline failed",
            exc_info=True,
        )

        state["error"] = str(e)

    return state


# -----------------------------------
# MAIN
# -----------------------------------

if __name__ == "__main__":

    topic = input("\nEnter research topic: ")

    result = run_research_pipeline(topic)

    print("\n" + "=" * 60)

    if "error" in result:

        print("ERROR:")
        print(result["error"])

    else:

        print("\nFINAL REPORT:\n")
        print(result["report"])

        print("\n" + "=" * 60)

        print("\nCRITIC FEEDBACK:\n")
        print(result["feedback"])
