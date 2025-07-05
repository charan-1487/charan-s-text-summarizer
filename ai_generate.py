# ai_generate.py

import google.generativeai as genai
import os

# Set your Gemini API key here or using environment variable
GOOGLE_API_KEY = "AIzaSyDgurWuozyOHTHJLGh06oc_83Jv1cUqMIc"
genai.configure(api_key=GOOGLE_API_KEY)

# Create a Gemini 1.5 Flash model
model = genai.GenerativeModel('models/gemini-1.5-flash')

def generate_summary(text):
    prompt = f"Summarize the following text:\n\n{text}"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
