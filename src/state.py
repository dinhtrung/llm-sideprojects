from typing import TypedDict, Optional, Dict, Any, List

from pydantic import BaseModel


# ======================================================
# ✅ STATE
# ======================================================

class AnalyzerDeps(BaseModel):
    file_path: Optional[str] = None

class TransactionSummary(BaseModel):
    row_count: int
    total_spent: float
    category_totals: Dict[str, float]
    top_transactions: List[Dict[str, Any]]
    raw: List[Dict[str, Any]]


class InsightResult(BaseModel):
    insights: Dict[str, Any]


class AdviceResult(BaseModel):
    advice: List[str]


class ReportResult(BaseModel):
    report: str
