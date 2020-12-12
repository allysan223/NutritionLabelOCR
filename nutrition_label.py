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
from collections import Counter

# show boxes around words detected by pytesseract
def printboxes(imageName):
    # detect words
    img = cv2.imread('images/'+imageName)
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    print(d.keys())

    # generate boxes around words
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # #show boxes
    cv2.imshow('img', img)
    cv2.waitKey(0)

def calcAccuracy(GTFile, label):
    #read in ground truth
    with open("./groundtruth/"+GTFile, "r") as f:
        GTtext = f.read()
        #check number of characters that match
        numMatches = sum((Counter(GTtext) & Counter(label.labelString())).values())
        total = len(GTtext)
        accuracy = numMatches/total * 100
        #print(accuracy)
    return accuracy


# get list of images from image set
images = []
currentDir = dirname(__file__)
filePath = join(currentDir, "./images")
for fileName in os.listdir(filePath):
    if fileName.lower().endswith(('.png', '.jpg', '.jpeg')):
        images.append(fileName)


# Get list of ground truths
GTfiles = []
for GTfileName in os.listdir('./groundtruth'):
    if GTfileName.lower().endswith(('.txt')):
        GTfiles.append(GTfileName)

#images = ["vanillaproteinpowder.jpg"]
fileText = ""

# read image
for image in images:
    # Run OCR on each image
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

    #find matching ground truth file if exists
    for GTfile in GTfiles:
        if GTfile.split(".")[0] == image.split(".")[0]:
            accuracy = calcAccuracy(GTfile, label1)
            print(accuracy)
            fileText = fileText + "\nAccuracy: " + str(accuracy)
            break

    #check if contains added sugars
    print("Contains added sugar:", str(label1.containsSugar()))
    fileText = fileText + "\nContains added sugar: " + str(label1.containsSugar())
    
    #end of label
    fileText = fileText + "\n--------------------------------------\n"
    print("--------------------------------------")
    # img = cv2.imread('images/label.png')

# Save data log to text file
with open("data.txt", "w") as file:
    file.write(fileText)



