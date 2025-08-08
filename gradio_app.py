import gradio as gr
from llm import llm

# Chat function using new "messages" format
def chat_with_model(message, history):
    response = llm(message)
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": response})
    return history

# Launching with styled UI
with gr.Blocks(
    theme=gr.themes.Soft(primary_hue="blue", secondary_hue="gray"),
   css="""
.gradio-container {
    font-family: 'Segoe UI', sans-serif;
    background: #1B1B1B;
}
.gr-textbox {
    border-radius: 10px;
    border: 1px solid #808080;
}
.gr-button {
    border-radius: 8px;
    font-weight: bold;
    padding: 10px 16px;
}
.gr-button:hover {
    background-color: #2563eb !important;
    color: white !important;
}
.gr-chatbot {
    border: 1px solid #e5e7eb;
    border-radius: 10px;
    background: #808080;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

/* Chat message bubbles */
.message.assistant {
    background-color: #A78BFA !important;
    color: white !important;
    border-radius: 10px;
    padding: 10px;
}
.message.user {
    background-color: #4B5563 !important;
    color: white !important;
    border-radius: 10px;
    padding: 10px;
}
"""

) as demo:
    gr.Markdown(
        """
        <div style='text-align: center;'>
            <h2 style='margin-bottom: 0.5em;'> Mistral Assistant (Local LLM)</h2>
            <p style='color: gray;'>Private, local AI model — fully offline and privacy-preserving.</p>
        </div>
        """
    )

    chatbot = gr.Chatbot(label=" Assistant", type="messages", height=450)

    with gr.Row():
        msg = gr.Textbox(
            placeholder="Type your question here...",
            label="Your Message",
            scale=9
        )
        send_btn = gr.Button(" Send", scale=1)

    state = gr.State([])

    send_btn.click(
        fn=chat_with_model,
        inputs=[msg, state],
        outputs=[chatbot],
        show_progress=True
    ).then(
        fn=lambda: "",
        outputs=msg
    )

demo.launch()
