import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_grid(image_path):
    # Read and preprocess image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use pytesseract to get text
    text = pytesseract.image_to_string(gray, config='--psm 6')

    # Clean and split into grid
    lines = [line.strip().replace(" ", "") for line in text.split("\n") if line.strip()]
    grid = [list(line.upper()) for line in lines]
    return grid
