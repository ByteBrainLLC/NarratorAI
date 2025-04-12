import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes documents."},
            {"role": "user", "content": f"Please summarize the following:\n\n{text}"}
        ],
        temperature=0.5
    )
    summary = response['choices'][0]['message']['content']
    return summary
