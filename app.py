import streamlit as st
from PIL import Image
from ocr import extract_text  # Import your OCR function from ocr.py
import re

# Function to highlight the keyword in the text
def highlight_text(text, keyword):
    # Using regex to wrap the keyword with a <span> tag for highlighting
    highlighted_text = re.sub(f'({keyword})', r'<mark>\1</mark>', text, flags=re.IGNORECASE)
    return highlighted_text

st.title("OCR with Keyword Search")
st.write("Upload an image with text in both Hindi and English, and search for keywords.")

# File uploader
image_file = st.file_uploader("Upload an image", type=["jpeg", "jpg", "png"])

if image_file:
    # Display the uploaded image
    img = Image.open(image_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Extract text using the OCR function
    extracted_text = extract_text(image_file)

    # Display extracted text
    st.write("Extracted Text:")
    st.text_area("Extracted Text", extracted_text, height=300)

    # Search bar below the extracted text
    keyword = st.text_input("Enter a keyword to search")

    # If a keyword is entered, perform the search
    if keyword:
        # Highlight the keyword in the extracted text
        highlighted_text = highlight_text(extracted_text, keyword)

        # Display highlighted text using markdown with HTML rendering
        st.markdown(f"<div style='font-size: 16px;'>{highlighted_text}</div>", unsafe_allow_html=True)

        # Indicate whether the keyword was found or not
        if re.search(keyword, extracted_text, re.IGNORECASE):
            st.success(f"Keyword '{keyword}' found!")
        else:
            st.error(f"Keyword '{keyword}' not found.")
