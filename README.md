# OCR and Keyword Search Web Application

This project is a web-based prototype that allows users to perform Optical Character Recognition (OCR) on an uploaded image containing text in both Hindi and English, and provides a basic keyword search functionality. The application is accessible via a live URL.

## Features

- Upload an image (JPEG, PNG) containing text.
- Perform OCR to extract both Hindi and English text from the image.
- Search for keywords in the extracted text and highlight them.
- Supports filtering out Hindi digits, keeping only Hindi characters when detecting Hindi text.

## Technologies Used

- Python
- Streamlit (for web interface)
- **EasyOCR** (for text extraction)
- Pillow (for image handling)
- Regular Expressions (for filtering Hindi digits and highlighting text)

## Installation

### Prerequisites
- Python 3.x

### Steps

1. **Clone this repository**:
   ```bash
   git clone [https://github.com/your-repo-url.git](https://github.com/tomar-sahab07/OCR_WebApp)
   
2. **Navigate to the project directory**:
   ```bash
   cd project-folder

3. **Create and activate a virtual environment**:
   - For Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - For Mac/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
4. **Install the required dependencies**:
     ```bash
     pip install -r requirements.txt
     
5. **Run the Streamlit web application**:
   ```bash
   streamlit run app.py

6. **Access the application**:
      - Open the following URL in your browser: [http://localhost:8501](http://localhost:8501)


## Usage
1. Upload an image containing text in both Hindi and English.
2. The extracted text will be displayed on the screen.
3. Enter a keyword in the search box to highlight matching words in the extracted text.

## Dependencies

- **Python**: Programming language used to write the application.
- **Streamlit**: Framework for building web apps in Python.
- **EasyOCR**: OCR tool for extracting text from images.
- **Pillow**: Image processing library used to handle image uploads.
- **Regular Expressions**: For searching and highlighting keywords within extracted text.


## Deployment
The application can be deployed using platforms like Streamlit Sharing, Hugging Face, or any other suitable platform.






