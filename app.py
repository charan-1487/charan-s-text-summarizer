# app.py

import streamlit as st
from ai_generate import generate_summary

st.set_page_config(page_title="Text Summarizer - Gemini 1.5 Flash")

st.title("📄 Text Summarizer with Gemini 1.5 Flash")
st.write("Enter or paste your text below, and get a quick summary using Gemini Flash.")

input_text = st.text_area("Enter text to summarize", height=300)

if st.button("Summarize"):
    if input_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Generating summary..."):
            summary = generate_summary(input_text)
        st.subheader("🔍 Summary:")
        st.success(summary)
