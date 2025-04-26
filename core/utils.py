import gradio as gr

def reset_textbox():
    return gr.update(value="")

def set_visible_false():
    return gr.update(visible=False)

def set_visible_true():
    return gr.update(visible=True)
