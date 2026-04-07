from pydantic import BaseModel
from pydantic_ai import Agent
from llm import chat_model


class RouterIntent(BaseModel):
    intent: str


# ---------- ROUTER AGENT ----------

router_prompt = """
You are a finance assistant routing engine.
Classify the user's request into one of the following intents:

- analyze_spending
- financial_advice
- generate_report
- other

Answer using ONLY a JSON object: {"intent": "..."}.
"""

router_agent = Agent(
    model=chat_model,
    output_type=RouterIntent,
    system_prompt=router_prompt

)
