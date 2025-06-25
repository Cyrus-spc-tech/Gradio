# sentimantal analysis using Gradio
import gradio as gr
from transformers import pipeline

# Load the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")
def analyze_sentiment(text):
    # Use the pipeline to analyze the sentiment of the input text
    result = sentiment_pipeline(text)
    return result[0]['label'], result[0]['score']

