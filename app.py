import re
import streamlit as st
from PIL import Image
import pytesseract

# Setting up Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


# Function to perform OCR on an image
def extract_text_from_image(image):
    return pytesseract.image_to_string(image, lang='hin+eng')


# Function to highlight keywords in the extracted text
def highlight_keywords(text, keyword):
    # Escaping keyword to handle special characters in regex
    escaped_keyword = re.escape(keyword)
    # Highlighting the keyword by wrapping it with HTML bold tags
    highlighted_text = re.sub(f"({escaped_keyword})", r"<mark>\1</mark>", text, flags=re.IGNORECASE)
    return highlighted_text


# Streamlit App
st.title("OCR and Keyword Search")

# Uploading image
uploaded_image = st.file_uploader("Upload an image containing Hindi and English text", type=['jpg', 'jpeg', 'png'])

if uploaded_image is not None:
    # Loading and displaying the image
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Extracting text from the image
    extracted_text = extract_text_from_image(image)

    # Displaying the extracted text
    st.subheader("Extracted Text")
    st.write(extracted_text)

    # Keyword search
    keyword = st.text_input("Enter a keyword to search in the extracted text")

    if keyword:
        # Highlighting the keyword in the extracted text
        highlighted_result = highlight_keywords(extracted_text, keyword)

        # Displaying the highlighted result as HTML
        st.subheader("Search Results")
        st.markdown(f"<div>{highlighted_result}</div>", unsafe_allow_html=True)
