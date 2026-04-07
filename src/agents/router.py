class RouterIntent(BaseModel):
    intent: str


router_agent = Agent(
    model="gpt-4o-mini",
    result_type=RouterIntent,
    system_prompt="""
You classify finance requests.
Return one of: analyze_spending, financial_advice, generate_report, other.
Respond with: {"intent": "..."}.
"""
)