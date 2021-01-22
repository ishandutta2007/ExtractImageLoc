# from PIL.Image import core as image
try:
    from PIL import Image
except ImportError:
    import Image
# from tesseract import image_to_string
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract"

from pytesseract import Output
import cv2
image_file_name="main-qimg-26b8862ecb375ab99700168c86d683e6.png"

# text = pytesseract.image_to_string(
#     Image.open("main-qimg-26b8862ecb375ab99700168c86d683e6.png")
# )
# # print(text)
# # print image_to_string(Image.open('test-english.jpg'), lang='eng')

# # Get bounding box estimates
# boxes = pytesseract.image_to_boxes(
#     Image.open("main-qimg-26b8862ecb375ab99700168c86d683e6.png")
# )

# print(boxes)


img = cv2.imread(image_file_name)

d = pytesseract.image_to_data(img, output_type=Output.DICT)
print("d:")
print(d)

print()
print()
for key, value in d.items():
    print(key, len(value))

for i in range(0, len(d["level"])):
    if int(d["conf"][i]) > 90 and len(d["text"][i]) > 1:
        print(
            d["text"][i],
            "=>",
            d["left"][i],
            d["top"][i],
            d["height"][i],
            d["width"][i],
            d["conf"][i],
        )

# n_boxes = len(d['level'])
# print(n_boxes)

# for i in range(n_boxes):
#     (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# cv2.imshow('img', img)
# cv2.waitKey(0)
