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
import os


# get list of images from image set
images = []
currentDir = dirname(__file__)
filePath = join(currentDir, "./images")
for fileName in os.listdir(filePath):
    if fileName.lower().endswith(('.png', '.jpg', '.jpeg')):
        images.append(fileName)

images = ["OAT.jpg"]

fileText = ""

# read image
for image in images:
    fileText = fileText + image + "\n********RAW DATA:*******\n"
    print(image)
    img = cv2.imread('images/'+image)
    # configure tesseract ocr
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(img, config=custom_config)
    fileText = fileText + text
    print(text)
    #parse text into label
    label1 = Label(text)
    fileText = fileText + "\n**********PARSE DATA:*********\n"+label1.labelString()
    label1.labelPrint()
    fileText = fileText + "--------------------------------------\n"
    print("--------------------------------------")
    # img = cv2.imread('images/label.png')

with open("data.txt", "w") as file:
    file.write(fileText)

#detect words
# d = pytesseract.image_to_data(img, output_type=Output.DICT)
# print(d.keys())

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

# # configure tesseract ocr
# custom_config = r'--oem 3 --psm 6'
# text = pytesseract.image_to_string(img, config=custom_config)
# print(text)
# #parse text into label
# label1 = Label(text)
# label1.labelPrint()
# print(label1.servingSize)