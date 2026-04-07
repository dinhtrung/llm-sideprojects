advice_agent = Agent(
    model="gpt-4o-mini",
    result_type=AdviceResult,
    system_prompt="""
You produce actionable financial advice based on insights.
Return: {"advice": [...]}.
"""
)