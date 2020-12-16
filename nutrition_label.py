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
from tabulate import tabulate

# show boxes around words detected by pytesseract
def printboxes(imageName, mode = "words"):

    img = cv2.imread('images/'+imageName)

    # detect words
    if mode == "words":
        d = pytesseract.image_to_data(img, output_type=Output.DICT)
        print(d.keys())

        # generate boxes around words
        n_boxes = len(d['text'])
        for i in range(n_boxes):
            if int(d['conf'][i]) > 60:
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    #detect characters
    else:
        h, w, c = img.shape
        boxes = pytesseract.image_to_boxes(img) 
        for b in boxes.splitlines():
            b = b.split(' ')
            img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

    # #show boxes
    cv2.imshow('img', img)
    cv2.waitKey(0)

def calcAccuracy(GTFile, label):
    #read in ground truth for label
    with open("./groundtruth/"+GTFile, "r") as f:
        GTtext = f.read()
        #check number of characters that match
        numMatches = sum((Counter(GTtext) & Counter(label.labelString())).values())
        total = len(GTtext)
        accuracy = numMatches/total * 100
        #print(accuracy)
    return accuracy

printboxes('mac.jpg')

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

#initialize variables
fileText = "" #text for log
labelData = {} #stores label data - image name, has sugar, accuracy

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

    #check if contains added sugars
    hasSugar = label1.containsSugar()
    print("Contains added sugar:", str(hasSugar))
    fileText = fileText + "\nContains added sugar: " + str(hasSugar)

    #find matching ground truth file if exists
    for GTfile in GTfiles:
        if GTfile.split(".")[0] == image.split(".")[0]:
            accuracy = calcAccuracy(GTfile, label1)
            print(accuracy)
            fileText = fileText + "\nAccuracy: " + str(accuracy)
            # add label data
            labelData[image] = (hasSugar, "{:.2f}".format(accuracy))
            break
        else:
            labelData[image] = (hasSugar, "")

    
    #labelData[image] = (hasSugar, "{:.2f}".format(accuracy))
    
    #end of label
    fileText = fileText + "\n--------------------------------------\n"
    print("--------------------------------------")
    # img = cv2.imread('images/label.png')

# Save data log to text file
with open("data.txt", "w") as file:
    file.write(fileText)

# tabulate added sugars
headers = ["Label Image", "Added Sugars?", "Accuracy"] 
print(tabulate([(k,) + v for k,v in labelData.items()], headers = headers)) 
#print(tabulate(labelData.items(), headers = headers))



