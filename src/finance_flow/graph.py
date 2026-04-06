from typing import List, TypedDict

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.constants import END
from langgraph.graph import StateGraph

from .llm import llm


# ---- Functions -----
def classify_intent(user_input: str) -> str:
    """
    Based on user input prompt, try to classify intent.
    :param user_input: the prompt from user
    :return:
    """
    classify_agent = create_agent(
        model=llm,
        system_prompt=SystemMessage(content="""
You are an intent classifier for a finance system.
Classify the user's message into one of:
["analyze_spending", "financial_advice", "upload_data", "budget_planning", "other"]
Return String represent the intent
        """)
    )
    return classify_agent.invoke({"messages": [
        HumanMessage(content=user_input)
    ]})["messages"][-1].content # return the content of the last message


def parse_transactions(user_input: str) -> List[dict]:
    return llm.invoke([
        SystemMessage(content="""
You are a financial data processor.
Input: raw text or CSV rows.
Output: categorized transactions in JSON. If unsure, guess category by description.
        """),
        HumanMessage(content=user_input)
    ]).content

def generate_insights(transactions: List[dict]) -> dict:
    return llm.invoke([
        SystemMessage(content="""
Analyze spending patterns: overspending areas, category ratios, and trends.
Output JSON with 3 sections:
1. Key insights
2. Potential risks
3. Notable patterns
        """),
        HumanMessage(content=f"Transactions: {transactions}")
    ]).content

def generate_advice(insights: dict) -> dict:
    return llm.invoke([
        SystemMessage(content="""
Based on insights + user profile, generate practical personal finance suggestions.
Focus on saving, debt control, subscription trimming, and spending alignment with goals.
Format as: {"advice": [...]}
        """),
        HumanMessage(content=f"Insights: {insights}")
    ]).content

def format_report(insights, advice) -> str:
    return llm.invoke([
        SystemMessage(content="""
Convert insights + advice into a friendly financial report in Markdown.
Include:
- Summary
- Category pie insights
- Action plan
- One motivational tip
        """),
        HumanMessage(content=f"Insights: {insights}\nAdvice: {advice}")
    ]).content




# ---- State -----
class FinanceState(TypedDict):
    user_input: str
    intent: str | None
    transactions: List[dict] | None
    insights: dict | None
    advice: dict | None
    report: str | None

# ---- Nodes -----
def router_node(state: FinanceState):
    # Call LLM to classify intent
    intent = classify_intent(state["user_input"])
    state["intent"] = intent
    return state

def analyze_node(state: FinanceState):
    tx = parse_transactions(state["user_input"])
    state["transactions"] = tx
    return state

def insight_node(state: FinanceState):
    ins = generate_insights(state["transactions"])
    state["insights"] = ins
    return state

def advice_node(state: FinanceState):
    adv = generate_advice(state["insights"])
    state["advice"] = adv
    return state

def report_node(state: FinanceState):
    rpt = format_report(state["insights"], state["advice"])
    state["report"] = rpt
    return state

# ---- Graph -----
graph = StateGraph(FinanceState)

graph.add_node("router", router_node)
graph.add_node("analyze", analyze_node)
graph.add_node("insight", insight_node)
graph.add_node("advice", advice_node)
graph.add_node("report", report_node)

graph.set_entry_point("router")

graph.add_conditional_edges(
    "router",
    lambda s: s["intent"],
    {
        "analyze_spending": "analyze",
        "financial_advice": "advice",
        "budget_planning": "advice",
        "upload_data": "analyze",
        "other": END
    }
)

graph.add_edge("analyze", "insight")
graph.add_edge("insight", "advice")
graph.add_edge("advice", "report")
graph.add_edge("report", END)

flow = graph.compile()
