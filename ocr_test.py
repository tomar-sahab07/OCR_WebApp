import pytesseract
from PIL import Image

def extract_text(image_file):
    img = Image.open(image_file)
    text = pytesseract.image_to_string(img, lang='eng+hin')  # OCR for both English and Hindi
    return text
