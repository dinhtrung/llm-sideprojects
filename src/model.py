
# ======================================================
# ✅ STATE
# ======================================================

class FinanceState(TypedDict):
    user_input: str
    file_path: Optional[str]
    intent: Optional[str]
    transactions: Optional[Dict[str, Any]]
    insights: Optional[Dict[str, Any]]
    advice: Optional[Dict[str, Any]]
    report: Optional[str]
    messages: List[Dict[str, str]]
