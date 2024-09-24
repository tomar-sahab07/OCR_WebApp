# app.py

import streamlit as st
from ocr import extract_text

def highlight_text(text, keyword):
    highlighted = text.replace(keyword, f"<mark>{keyword}</mark>")
    return highlighted

st.title("OCR Text Extraction")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    with open("temp_image.png", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Extract text
    extracted_text = extract_text("temp_image.png")
    st.write("Extracted Text:")
    st.write(extracted_text)
    
    # Keyword search
    keyword = st.text_input("Enter keyword to search:")
    
    if keyword:
        highlighted_text = highlight_text(extracted_text, keyword)
        st.markdown(highlighted_text, unsafe_allow_html=True)
