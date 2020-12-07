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
import matplotlib.image as mpimg
from os.path import dirname, join
from label import *

# current_dir = dirname(__file__)
# file_path = join(current_dir, "./label.png")
# img = cv2.imread(file_path)

img = cv2.imread('label.png')
# plt.imshow(img)
# plt.show()

# Adding custom options
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, config=custom_config)
print(text)

label1 = Label(text)
print(label1.ingredients)