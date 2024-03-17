import cv2
import numpy as np

img = cv2.imread("14-1.jpg")
cv2.imshow("img",img)
gauss = cv2.GaussianBlur(img,(7,7),0)#高斯滤波器 ，内核设置为五个像素   #奇数
cv2.imshow("gauss",gauss)
median = cv2.medianBlur(gauss,7) #中值滤波器
cv2.imshow("median",median)
binary=cv2.morphologyEx(median, cv2.MORPH_OPEN,(9,9))
binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE,(9,9))

cv2.imshow("binary",binary)
cv2.waitKey()