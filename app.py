import gradio as gr
from caption import generate_caption

demo = gr.Interface(
    fn=generate_caption,
    inputs=gr.Image(type="pil", label="Upload an Image"),
    outputs=gr.Textbox(label="Generated caption"),
    title="AI ImageCaption Generator",
    description="Upload an image and let the BLIP midel describe it."
)

demo.launch()