
import cv2
import numpy as np

# 读取一张图片
image = cv2.imread("9.png")

# 使用Canny函数进行边缘检测
edges = cv2.Canny(image, 100, 200)

# 显示结果
cv2.imshow('Original', image)
cv2.imshow('Canny Edges', edges)
cv2.waitKey()
