from typing import Optional

from pydantic_ai import AgentRunResult

from agents.advice import advice_agent
from agents.analyzer import analyzer_agent
from agents.insight import insight_agent
from agents.report import report_agent
from agents.router import router_agent
from state import AnalyzerDeps


def debug_run(result: AgentRunResult):
    print(f"Agent: {result.response}")

async def finance_flow(user_input: str, file_path: Optional[str] = None):
    # 1. Route
    route = await router_agent.run(user_input)
    debug_run(route)
    intent = route.output.intent
    print(f"Intent: {intent}")

    # ----- ANALYZE SPENDING -----
    if intent == "analyze_spending":
        analysis = await analyzer_agent.run(f"Analyze the content of this file: {file_path}")
        debug_run(analysis)
        summary = analysis.output.summary

        # Insights
        print(f"user_input: {user_input} deps: {summary.dict()}")
        insights = await insight_agent.run(user_input, deps=summary.dict())
        debug_run(insights)
        advice = await advice_agent.run(user_input, deps=insights.output.insights)
        debug_run(advice)

        # Report
        report = await report_agent.run(user_input, deps={
            "insights": insights.output.insights,
            "advice": advice.output.advice
        })

        return {
            "summary": summary,
            "insights": insights.output.insights,
            "advice": advice.output.advice,
            "report": report.output.report
        }

    # ----- GENERAL ADVICE -----
    if intent == "financial_advice":
        insights = await insight_agent.run(user_input)
        debug_run(insights)
        advice = await advice_agent.run(user_input, deps=insights.output.insights)
        debug_run(advice)

        return {
            "insights": insights.output.insights,
            "advice": advice.output.advice
        }

    # ----- GENERATE REPORT -----
    if intent == "generate_report":
        report = await report_agent.run(user_input)
        debug_run(report)
        return {"report": report.output.report}

    # ----- FALLBACK -----
    return {"message": "I didn't understand your request."}