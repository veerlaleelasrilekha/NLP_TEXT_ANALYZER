import gradio as gr
from google import genai

# ----------------------------
# Gemini API Key
# ----------------------------
client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

# ----------------------------
# NLP Functions
# ----------------------------
def summarize(text):
    prompt = f"Summarize the following text:\n\n{text}"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def sentiment(text):
    prompt = f"Analyze the sentiment of the following text and explain whether it is Positive, Negative, or Neutral:\n\n{text}"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def translate(text):
    prompt = f"Translate the following text into Telugu:\n\n{text}"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def keywords(text):
    prompt = f"Extract the important keywords from the following text:\n\n{text}"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

# ----------------------------
# Gradio Interface
# ----------------------------
with gr.Blocks(title="NLP Full Stack App") as demo:
    gr.Markdown("# NLP Full Stack Application")

    text = gr.Text
