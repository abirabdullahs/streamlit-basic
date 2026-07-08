import streamlit as st

st.title("Text Display App")

# User Input
text = st.text_input("Enter a text:")

# Input empty হলে কিছুই দেখাবে না
if text:

    st.divider()
    st.title(text)

    st.divider()
    st.header(text)

    st.divider()
    st.subheader(text)

    st.divider()
    st.text(text)
