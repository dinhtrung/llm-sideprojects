class AnalyzerOutput(BaseModel):
    summary: TransactionSummary


analyzer_agent = Agent(
    model="gpt-4o-mini",
    result_type=AnalyzerOutput,
    tools=[load_csv_transactions],
    system_prompt="""
If file_path is provided, call load_csv_transactions(file_path).
Return the structured summary.
"""
)