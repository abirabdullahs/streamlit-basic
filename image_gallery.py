import streamlit as st

img = st.file_uploader(
    "Upload Images",
    type=["jpg", "png"],
    accept_multiple_files=True
)

if img:
    if len(img) > 3:
        st.error("You can't upload more than 3 images.")

    elif len(img) == 3:
        st.success("Upload successful!")

        cols = st.columns(3)

        for i, pimg in enumerate(img):
            cols[i].image(pimg)
