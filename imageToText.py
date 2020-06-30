from tkinter import *
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open('pic.png')
text = tess.image_to_string(img)

if len(text) == 0:
    text = "Please Try Agian With Clearly words"


win = Tk()

win.geometry("300x200")
win = Label(text=text)
win.pack()


