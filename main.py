import gradio as gt 
def greet(name):
    return f"Hello, {name}!"

demo = gt.Interface(fn=greet, inputs="text", outputs="text")


demo.launch(share=True)