# Streamlit Practice Problems

This repository contains solutions to five Streamlit practice problems.

## Prerequisites

Install the required packages:

```bash
pip install streamlit google-genai python-dotenv
```

Run any app using:

```bash
streamlit run app.py
```

---

# Problem 1: Multiple Image Uploader

### Problem Statement

Create a Streamlit app where users can upload multiple images.

### Requirements

- Use `st.file_uploader()`
- Accept only `jpg` and `png` images
- Allow multiple image uploads
- Show an error if more than 3 images are uploaded
- If exactly 3 images are uploaded, show a success message
- Display the uploaded images in separate columns

---

# Problem 2: Audio & Video Player

### Problem Statement

Create a Streamlit app where users can upload an audio or video file and play it after clicking a button.

### Requirements

- Use separate `st.file_uploader()` widgets
- Audio formats: `mp3`, `ogg`
- Video formats: `mp4`, `mkv`
- Show a **Play** button
- Do not display the player before clicking the button
- Show `st.error()` if the button is clicked without uploading any file

---

# Problem 3: Text Display App

### Problem Statement

Create a Streamlit app where users enter a text and the same text is displayed using different Streamlit text functions.

### Requirements

- Take input using `st.text_input()`
- Display the text using:
  - `st.title()`
  - `st.header()`
  - `st.subheader()`
  - `st.text()`
- Separate each section using `st.divider()`
- Display nothing if the input is empty

---

# Problem 4: Gemini AI Prompt Generator

### Problem Statement

Create a Streamlit app that takes a prompt from the user and generates a response using the Gemini API.

### Requirements

- Use `st.text_area()` for prompt input
- Read the API key from a `.env` file
- Generate a response using the Gemini API
- Display the generated response
- Show a warning if no prompt is entered

---

# Problem 5: Gemini API Integration

### Problem Statement

Integrate the Google Gemini API into a Streamlit application.

### Requirements

- Load the API key from `.env`
- Initialize the Gemini client
- Use the `gemini-2.5-flash` model
- Generate content based on user input
- Display the generated response

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- python-dotenv
