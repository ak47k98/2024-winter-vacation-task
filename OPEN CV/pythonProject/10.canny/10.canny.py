"""
canny
对输入图像进行灰度化处理。
对灰度图像进行高斯滤波，以平滑图像并去除噪声。
对滤波后的图像使用Sobel算子计算梯度幅值和方向。
对梯度幅值进行非极大值抑制，以压缩边缘带宽。
对压缩后的边缘带宽使用滞后阈值进行二值化，得到二值化图像。
对二值化图像进行连接操作，将断开的边缘进行连接，得到最终的边缘图像。


较低的阈值可以检测到较弱的边缘，而较高的阈值可以去除较弱的边缘
"""

import cv2
import numpy as np






# 读取一张图片
image = cv2.imread("9.png")


# 使用Canny函数进行边缘检测
edges = cv2.Canny(image, 100, 200)

laplacian = cv2.Laplacian(image,cv2.CV_64F)    #拉普拉斯算子  表示图像的二阶导数


# 显示结果
cv2.imshow('Original', image)
cv2.imshow('Canny Edges', edges)
cv2.imshow("laplacian",laplacian)
cv2.waitKey()
