from pydantic_ai import Agent, Tool
import pandas as pd

from state import TransactionSummary


@Tool
def load_csv_transactions(file_path: str) -> TransactionSummary:
    """Load and summarize the CSV file."""
    print(f"Loading CSV: {file_path}")
    df = pd.read_csv(file_path)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    return TransactionSummary(
        row_count=len(df),
        total_spent=float(df["amount"].sum()),
        category_totals=df.groupby("category")["amount"].sum().to_dict(),
        top_transactions=df.sort_values("amount", ascending=False)
                          .head(5)
                          .to_dict(orient="records"),
        raw=df.to_dict(orient="records")
    )