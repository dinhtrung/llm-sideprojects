insight_agent = Agent(
    model="gpt-4o-mini",
    result_type=InsightResult,
    system_prompt="""
You analyze spending summary and generate insights.
Return: {"insights": {...}}.
"""
)