import gradio as gr
from core.repo_analyzer import analyze_repo
from core.utils import reset_textbox, set_visible_false, set_visible_true


def analyze_repo_click(repo_url, progress=gr.Progress()):
    return analyze_repo(repo_url, progress)


def handle_input_submit():
    return reset_textbox(), set_visible_false(), set_visible_true()
