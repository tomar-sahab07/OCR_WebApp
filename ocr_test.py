# testing the image to text model here...

from PIL import Image
import pytesseract

# Setting the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Loading an image from local machine
image = Image.open("C:\\Users\\tomar\\OneDrive\\Documents\\hin_img.jpg")

# Using pytesseract to extract text from the image
extracted_text = pytesseract.image_to_string(image, lang='eng+hin')

# Printing the extracted text
print("Extracted Text:\n", extracted_text)
