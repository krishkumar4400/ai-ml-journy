import logging

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_ollama import ChatOllama

from langchain.agents import (
    AgentExecutor,
    create_react_agent,
)


from tools import web_search, scrape_url

# -----------------------------------
# Load env
# -----------------------------------

load_dotenv()

# -----------------------------------
# Logging
# -----------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

logger = logging.getLogger(__name__)

# -----------------------------------
# LLM
# -----------------------------------

llm = ChatOllama(
    model="gemma:7b",
    temperature=0,
)

# -----------------------------------
# ReAct Prompt
# -----------------------------------
# -----------------------------------
# ReAct Prompt
# -----------------------------------

from langchain_core.prompts import PromptTemplate

# -----------------------------------
# ReAct Prompt
# -----------------------------------

prompt = PromptTemplate.from_template("""
Answer the following questions as best you can.

You have access to the following tools:

{tools}

Tool Names:
{tool_names}

Use the following format:

Question: the input question you must answer

Thought: think about what to do

Action: the action to take, should be one of [{tool_names}]

Action Input: the input to the action

Observation: the result of the action

... (this Thought/Action/Action Input/Observation can repeat)

Thought: I now know the final answer

Final Answer: the final answer to the original question

Question: {input}

Thought: {agent_scratchpad}
""")

# -----------------------------------
# Search Agent
# -----------------------------------


def build_search_agent(verbose=True):

    agent = create_react_agent(
        llm=llm,
        tools=[web_search],
        prompt=prompt,
    )

    executor = AgentExecutor(
        agent=agent,
        tools=[web_search],
        verbose=verbose,
    )

    return executor


# -----------------------------------
# Reader Agent
# -----------------------------------


def build_reader_agent(verbose=True):

    agent = create_react_agent(
        llm=llm,
        tools=[scrape_url],
        prompt=prompt,
    )

    executor = AgentExecutor(
        agent=agent,
        tools=[scrape_url],
        verbose=verbose,
    )

    return executor


# -----------------------------------
# Writer Chain
# -----------------------------------

writer_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert research writer.

Write clear, professional,
well-structured research reports.
""",
        ),
        (
            "human",
            """
Write a detailed research report.

TOPIC:
{topic}

RESEARCH:
{research}

Structure:
1. Introduction
2. Key Findings
3. Conclusion
4. Sources

Be detailed and factual.
""",
        ),
    ]
)

writer_chain = writer_prompt | llm | StrOutputParser()

# -----------------------------------
# Critic Chain
# -----------------------------------

critic_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a strict research critic.
Provide honest feedback.
""",
        ),
        (
            "human",
            """
Review this report:

{report}

Respond in this format:

Score: X/10

Strengths:
- ...

Areas to Improve:
- ...

Verdict:
...
""",
        ),
    ]
)

critic_chain = critic_prompt | llm | StrOutputParser()
