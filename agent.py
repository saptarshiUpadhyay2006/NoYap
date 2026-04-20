from agno.agent import Agent

from agno.models.openai.responses import OpenAIResponses
from agno.models.groq import Groq

from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"),
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions="You are a helpful and expert travel agent."
    )

openai_agent=build_agent()

openai_agent.print_response("Is it safe to travel to Iran today?")