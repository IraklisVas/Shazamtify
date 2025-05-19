from PIL import Image
import pytesseract

def song():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = Image.open(r"")
    toText = pytesseract.image_to_string(img)
    print(toText)
    normalized = toText.replace('\n', '.')

    first_sentence = normalized.split('.')[0].strip() + ' '
    second_sentence = normalized.split('.')[1].strip()
    print(first_sentence + second_sentence)
    return first_sentence + second_sentence
