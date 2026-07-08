import streamlit as st

st.title("Audio & Video Player")

# Audio Upload
audio_file = st.file_uploader(
    "Upload an Audio File",
    type=["mp3", "ogg"]
)

# Video Upload
video_file = st.file_uploader(
    "Upload a Video File",
    type=["mp4", "mkv"]
)

# Play Button
if st.button("Play"):

    if audio_file is None and video_file is None:
        st.error("Please upload an audio or video file first.")

    else:
        if audio_file is not None:
            st.audio(audio_file)

        if video_file is not None:
            st.video(video_file)
