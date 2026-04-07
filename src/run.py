import gradio as gr
import asyncio


def analyze_csv(file):
    if not file:
        return "Please upload a file.", None, None, None

    result = asyncio.run(finance_flow("analyze my spending", file_path=file.name))

    summary = f"""
### ✅ Summary
- Total Rows: {result['summary'].row_count}
- Total Spent: **${result['summary'].total_spent:.2f}**
"""

    df = pd.DataFrame(result["summary"].raw)
    cat_df = pd.DataFrame(
        list(result["summary"].category_totals.items()),
        columns=["category", "amount"]
    )

    return summary, df.head(), cat_df, "Done."


def chat_with_agent(msg, history):
    result = asyncio.run(finance_flow(msg))

    reply = result.get("report") or \
            str(result.get("advice") or result.get("insights") or result)

    history.append((msg, reply))
    return history, ""


with gr.Blocks() as demo:
    gr.Markdown("# Finance Flow (PydanticAI + Gradio + Qdrant)")

    with gr.Tab("CSV Analysis"):
        file_input = gr.File()
        out1 = gr.Markdown()
        out2 = gr.DataFrame()
        out3 = gr.DataFrame()
        out4 = gr.Markdown()
        btn = gr.Button("Analyze")

        btn.click(analyze_csv, [file_input], [out1, out2, out3, out4])

    with gr.Tab("Chat"):
        chatbot = gr.Chatbot()
        msg = gr.Textbox()
        btn2 = gr.Button("Send")
        btn2.click(chat_with_agent, [msg, chatbot], [chatbot, msg])

demo.launch()