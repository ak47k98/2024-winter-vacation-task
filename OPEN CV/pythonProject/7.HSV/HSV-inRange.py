import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("配图2.jpg")
hsvimage = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

lower_threshold = np.array([0,100,100])
upper_threshold = np.array([20,255,255])
mask = cv2.inRange(hsvimage,lower_threshold,upper_threshold)
redone = cv2.bitwise_and(image,image,mask=mask)


lower_threshold = np.array([100, 50, 50])
upper_threshold = np.array([130, 255, 255])
mask = cv2.inRange(hsvimage,lower_threshold,upper_threshold)
blueone = cv2.bitwise_and(image,image,mask=mask)

cv2.imshow("redone",redone)
cv2.imshow("blueone",blueone)
cv2.waitKey()