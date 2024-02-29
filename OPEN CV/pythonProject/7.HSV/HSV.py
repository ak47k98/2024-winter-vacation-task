import cv2
import numpy as np


image =cv2.imread("配图2.jpg")
height, width,_=image.shape()
cv2.imshow("base",image)
cv2.namedWindow()

