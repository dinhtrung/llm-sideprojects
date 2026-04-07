from pydantic_ai.agent import Agent

from llm import chat_model
from state import AdviceResult

advice_prompt = """
You are a personal finance coach.

Using insights, generate:
- 3–5 actionable pieces of advice
- Budget suggestions
- Priority steps

Return JSON: {"advice": [...]}
"""

advice_agent = Agent(
    model=chat_model,
    output_type=AdviceResult,
    system_prompt=advice_prompt
)
