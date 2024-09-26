import streamlit as st
import easyocr
from PIL import Image
import numpy as np
import re


# Function to filter out Hindi digits and keep only Hindi characters for Hindi text
def filter_hindi_text(text):
    # Regular expression to match Hindi text (Devanagari script) while excluding Hindi digits
    hindi_text_only = re.sub(r'[०१२३४५६७८९]', '', text)  # Removes Hindi digits
    return hindi_text_only


# Function to perform OCR on the image using EasyOCR
def extract_text(image, languages):
    reader = easyocr.Reader(languages)  # Specify languages you want (Hindi and English)
    result = reader.readtext(np.array(image), detail=0)  # detail=0 gives only the text

    filtered_result = []

    for line in result:
        if re.search(r'[ऀ-ॿ]', line):  # If the line contains Hindi characters
            filtered_result.append(filter_hindi_text(line))  # Filter Hindi text
        else:
            filtered_result.append(line)  # Keep English text as is

    return ' '.join(filtered_result)


# Function to highlight the searched keyword in the extracted text
def highlight_text(text, search_term):
    if not search_term:
        return text

    # Escape special characters for HTML
    escaped_search_term = re.escape(search_term)

    # Highlight the searched term by wrapping it in HTML <mark> tag
    highlighted_text = re.sub(f'({escaped_search_term})', r'<mark>\1</mark>', text, flags=re.IGNORECASE)

    return highlighted_text


# Streamlit app
def main():
    st.title("Hindi and English OCR App")

    st.write("Upload an image containing text in Hindi and/or English, and the app will extract the text.")

    # File uploader to upload images
    uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Open the uploaded image file
        image = Image.open(uploaded_file)

        # Display the image in the app
        st.image(image, caption='Uploaded Image', use_column_width=True)

        st.write("Extracting text...")

        # Specify the languages to be used for OCR (Hindi and English)
        extracted_text = extract_text(image, ['hi', 'en'])  # 'hi' for Hindi, 'en' for English

        st.write("Extracted Text:")

        # Display the extracted text first
        st.text_area("Extracted Text:", value=extracted_text, height=200)

        # Now, show the search bar below the extracted text
        search_term = st.text_input("Enter keyword to search within extracted text")

        if search_term:
            # Highlight the searched term in the extracted text
            highlighted_text = highlight_text(extracted_text, search_term)

            # Display the highlighted text using Markdown with unsafe HTML to allow highlighting
            st.markdown(highlighted_text, unsafe_allow_html=True)

            # Display a message if no match is found
            if search_term.lower() not in extracted_text.lower():
                st.write(f"'{search_term}' not found in the text.")


if __name__ == "__main__":
    main()
