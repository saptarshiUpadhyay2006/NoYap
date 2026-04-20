from agno.agent import Agent

from agno.models.openai.responses import OpenAIResponses
from agno.models.groq import Groq
from phi.tools.yfinance import YFinanceTools

from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"),
        tools=[YFinanceTools(),DuckDuckGoTools()],
        markdown=True,
        add_datetime_to_context=True,
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["Use given tools whenever possible.Format your response using markdown and use tables to display data where possible."],
        debug_mode=True
    )

openai_agent=build_agent()

openai_agent.print_response("Share the MSFT stock price in INR and analyst recommendations", markdown=True)