async def finance_flow(user_input: str, file_path: Optional[str] = None):
    # 1. Route
    route = await router_agent.run(user_input)
    intent = route.intent

    # ----- ANALYZE SPENDING -----
    if intent == "analyze_spending":
        analyzer_input = {
            "file_path": file_path
        }
        analysis = await analyzer_agent.run(analyzer_input)
        summary = analysis.summary

        # Insights
        insights = await insight_agent.run(summary.dict())
        advice = await advice_agent.run(insights.insights)

        # Report
        report = await report_agent.run({
            "insights": insights.insights,
            "advice": advice.advice
        })

        return {
            "summary": summary,
            "insights": insights.insights,
            "advice": advice.advice,
            "report": report.report
        }

    # ----- GENERAL ADVICE -----
    if intent == "financial_advice":
        insights = await insight_agent.run({"message": user_input})
        advice = await advice_agent.run(insights.insights)

        return {
            "insights": insights.insights,
            "advice": advice.advice
        }

    # ----- GENERATE REPORT -----
    if intent == "generate_report":
        report = await report_agent.run({"message": user_input})
        return {"report": report.report}

    # ----- FALLBACK -----
    return {"message": "I didn't understand your request."}