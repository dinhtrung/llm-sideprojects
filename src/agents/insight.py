from pydantic_ai import Agent

from llm import chat_model
from state import InsightResult

insight_prompt = """
You receive a summary of financial transactions.

Generate insights:
1. Top spending categories
2. Bad habits or patterns
3. Unusual spikes
4. Subscription creep
5. Savings opportunities

Respond as JSON: {"insights": {...}}
"""

insight_agent = Agent(
    model=chat_model,
    output_type=InsightResult,
    system_prompt=insight_prompt
)
