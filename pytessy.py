# from source 
import pytessy
# from pytessy import *
# PyTessy
from PIL import ImageFilter, Image
import sys

# import pyclbr
# print(pyclbr.readmodule('pytessy').keys())

ocrReader = pytessy.PyTessy()
file ="main-qimg-26b8862ecb375ab99700168c86d683e6.png"
img = Image.open(file)
w, h = img.size
img = img.resize((2 * w, 2 * h))
img = img.filter(ImageFilter.SHARPEN)
imgBytes = img.tobytes()
bytesPerPixel = int(len(imgBytes) / (img.width * img.height))
imageStr = ocrReader.read(img.tobytes(), img.width, img.height, bytesPerPixel, raw=True, resolution=600)
print(file, imageStr)
