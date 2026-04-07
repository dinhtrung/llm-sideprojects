from pydantic import BaseModel
from pydantic_ai import Agent

from state import TransactionSummary
from llm import chat_model
from tools.csv_loader import load_csv_transactions

# ---------- SPENDING ANALYZER AGENT ----------
analyzer_prompt = """
You analyze financial transaction summaries produced by tools.

If a file_path is provided, call the tool: load_csv_transactions.

Your goal:
- Load & summarize the CSV
- Explain key patterns
- Hand structured data to the next agent

Respond concisely.
"""


class AnalyzerOutput(BaseModel):
    summary: TransactionSummary


analyzer_agent = Agent(
    model=chat_model,
    output_type=AnalyzerOutput,
    tools=[load_csv_transactions],
    system_prompt=analyzer_prompt
)
