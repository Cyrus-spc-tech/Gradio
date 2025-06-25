import gradio as gr
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
def predict(text):
    return classifier(text)[0]

gr.Interface(fn=predict, inputs="text", outputs="text").launch()