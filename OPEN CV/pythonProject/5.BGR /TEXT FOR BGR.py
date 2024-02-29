import cv2
import copy
image = cv2.imread("配图2.jpg")
print(image.shape)#打印维度(横行,竖行,三原色彩色通道)  BGR格式存储
bimage, gimage, rimage = cv2.split(image)
cv2.imshow('blue', bimage)
cv2.imshow('green', gimage)
cv2.imshow('red', rimage)

image0=copy.deepcopy(image)
image0[:,:,0]=0
image0[:,:,1]=0
cv2.imshow('turered', image0)

cv2.waitKey()
