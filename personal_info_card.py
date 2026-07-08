import streamlit as st

name = st.text_input("Enter your name")
number = st.number_input("Enter your age", min_value=0)

occupation = st.selectbox(
    "Select your occupation",
    ["Student", "Teacher", "Businessman", "Others"]
)

if st.button("Generate"):
    if name and occupation:
        st.success(f"""
        Name: {name}
        Age: {number}
        Occupation: {occupation}
        """)
    else:
        st.warning("Please fill in all the required fields.")
