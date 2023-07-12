# pip install pytesseract

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open("news.png"), lang="kor")
print(text)

with open("news.txt", "w", encoding="utf8") as f:
    f.write(text)

