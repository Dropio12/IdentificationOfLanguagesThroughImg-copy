# text recognition
import cv2
import pytesseract
from PIL import Image
import os

def image_to_text(image):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Strea\AppData\Local\Tesseract-OCR\tesseract.exe'
    # read the image
    img = cv2.imread(image)
    # convert to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # apply threshold
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # save the filtered image in the /tmp directory
    filename = "{}.jpg".format(os.getpid())
    cv2.imwrite(filename, thresh)
    # load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(text)
    return text

text=image_to_text('ImageWithText.jpg')
print(text)