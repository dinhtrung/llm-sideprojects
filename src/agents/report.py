report_agent = Agent(
    model="gpt-4o-mini",
    result_type=ReportResult,
    system_prompt="""
You generate a polished financial report in Markdown.
Return: {"report": "..."}.
"""
)