import sys
import torch
import torchvision
import torchvision.transforms as transforms
import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
from cv2 import cv2
import math
import pytesseract
from pytesseract import Output
import matplotlib.image as mpimg
from os.path import dirname, join
from label import *


# current_dir = dirname(__file__)
# file_path = join(current_dir, "./label.png")
# img = cv2.imread(file_path)

img = cv2.imread('chocolateBar.png')

#detect words
d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())

#generate boxes around words
# n_boxes = len(d['text'])
# for i in range(n_boxes):
#     if int(d['conf'][i]) > 60:
#         (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#         img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# # #show boxes
# cv2.imshow('img', img)
# cv2.waitKey(0)

# plt.imshow(img)
# plt.show()

# Adding custom options
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, config=custom_config)
print(text)

label1 = Label(text)
label1.labelPrint()
print(label1.servingSize)