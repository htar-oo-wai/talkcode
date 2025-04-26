import gradio as gr
from ui.callbacks import analyze_repo_click, handle_input_submit
from constants import SYSTEM_MSG_INFO, TITLE_HTML

def build_interface():
    theme = gr.themes.Soft(text_size=gr.themes.sizes.text_md)

    with gr.Blocks(theme=theme, title="TalkCode") as demo:
        gr.HTML(TITLE_HTML)

        with gr.Column(elem_id="col_container"):
            with gr.Accordion(label="System message:", open=False):
                system_msg = gr.Textbox(label="Instruct the AI Assistant", info=SYSTEM_MSG_INFO)
                accordion_msg = gr.HTML(value="Refresh the app to reset system message", visible=False)

            with gr.Row():
                repo_url = gr.Textbox(placeholder="Repo Link", lines=1, label="Repo Link")
                repo_link_btn = gr.Button("Analyze Code Repo")
                analyze_progress = gr.Textbox(label="Status")

            repo_link_btn.click(analyze_repo_click, [repo_url], [system_msg, analyze_progress])

            chatbot = gr.Chatbot(label="TalkCode", elem_id="chatbot", type="messages")
            state = gr.State([])

            inputs = gr.Textbox(placeholder="What questions do you have for the repo?", lines=1)
            b1 = gr.Button()

            inputs.submit(handle_input_submit, [], [inputs, system_msg, accordion_msg])
            b1.click(handle_input_submit, [], [inputs, system_msg, accordion_msg])

    return demo
