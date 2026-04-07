from pydantic_ai import Agent

from llm import chat_model
from state import ReportResult

report_prompt = """
You produce a polished monthly financial report in markdown.

Inputs:
- insights
- advice

Format:
# Monthly Report
## Summary
## Category Breakdown
## Actionable Advice
## Call-to-Action
"""

report_agent = Agent(
    model=chat_model,
    output_type=ReportResult,
    system_prompt=report_prompt
)
