import gradio as gr
import pandas as pd


# ---------------------
# Mock Functions
# ---------------------

def analyze_transactions(file):
    if file is None:
        return "Please upload a CSV file.", None, None, None

    df = pd.read_csv(file.name)

    # Mock summary
    summary = f"""
### ✅ Spending Summary
- Total Rows: {len(df)}
- Total Amount: ${df['amount'].sum():,.2f}
- Categories: {', '.join(df['category'].unique())}
    """

    # Mock chart data
    chart_data = df.groupby("category")["amount"].sum().reset_index()

    return summary, df.head(), chart_data, "Analysis completed."


def chat_with_assistant(message, history):
    # Mock assistant response
    response = f"💬 *Assistant:* I received your message: **{message}**.\n\n(This is a mock response.)"
    history.append((message, response))
    return history, ""


def generate_report():
    return """
# 📊 Monthly Financial Report (Mock)

### Summary
- Total Spending: **$2,280**
- Savings Rate: **28.7%**
- Top Category: **Dining Out**

### Recommendations
- Reduce subscriptions by $20–30.
- Add weekly dining limits.
- Track impulse purchases.

_This is a mock generated report._
"""


# ---------------------
# UI Layout
# ---------------------

with gr.Blocks(title="Finance Flow (Mock UI)") as demo:
    gr.Markdown("# 💸 Finance Flow — Mock UI")
    gr.Markdown("A demo interface for your LangGraph-based financial assistant.")

    with gr.Tab("🏠 Dashboard"):
        with gr.Row():
            gr.Markdown("""
            ### ✅ Monthly Overview
            - Total Spending: **$2,280**
            - Savings Rate: **28.7%**
            - Top Category: **Dining**
            - Subscriptions: **$145**
            """)

        gr.Markdown("*(Mock static data for UI layout testing)*")

    with gr.Tab("📤 Upload & Analyze"):
        gr.Markdown("### Upload your transaction CSV")
        file_input = gr.File(file_types=[".csv"])

        analyze_btn = gr.Button("Analyze File")

        summary_output = gr.Markdown()
        df_output = gr.DataFrame()
        chart_output = gr.BarPlot(x="category", y="amount", title="Category Spend (Mock)")
        status = gr.Markdown()

        analyze_btn.click(
            analyze_transactions,
            inputs=file_input,
            outputs=[summary_output, df_output, chart_output, status]
        )

    with gr.Tab("💬 Chat Assistant"):
        chatbot = gr.Chatbot(height=400)
        msg = gr.Textbox(label="Ask something...")
        send_btn = gr.Button("Send")

        send_btn.click(chat_with_assistant, inputs=[msg, chatbot], outputs=[chatbot, msg])

    with gr.Tab("📑 Reports"):
        gr.Markdown("### Generate a Monthly Report")
        gen_btn = gr.Button("Generate Report")
        report_view = gr.Markdown()

        gen_btn.click(generate_report, outputs=report_view)

demo.launch()
