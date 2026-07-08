import streamlit as st
from google import genai

# Gemini Client
client = genai.Client(api_key="YOUR_API_KEY")

st.title("Gemini AI")

question = st.text_area("Enter your prompt here")

if st.button("Generate"):
    if question:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question
        )

        st.write(response.text)
    else:
        st.warning("Please enter a prompt.")
