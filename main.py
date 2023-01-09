
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

imagename = input("Image Name: ")

a=pytesseract.image_to_string(Image.open(imagename), lang="tur")

print(a)
open(imagename + ".txt", "a+").write(a)
