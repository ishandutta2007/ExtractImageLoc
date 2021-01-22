import tesserocr
from PIL import Image

image_file_name="main-qimg-26b8862ecb375ab99700168c86d683e6.png"
api = tesserocr.PyTessBaseAPI()
pil_image = Image.open(image_file_name)
api.SetImage(pil_image)
text = api.GetUTF8Text()
print(text)