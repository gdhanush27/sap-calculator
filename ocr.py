import pytesseract
from PIL import Image
import io

def extract_text_from_image(image):
    # Convert the image data to a PIL image
    image = Image.open(io.BytesIO(image))

    # Use Tesseract OCR to extract the text from the image
    text = pytesseract.image_to_string(image)

    return text
