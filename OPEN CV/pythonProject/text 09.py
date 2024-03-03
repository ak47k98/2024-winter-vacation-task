"""
import cv2
import numpy as np
gray = cv2.imread("9.png",cv2.IMREAD_GRAYSCALE)
ret,binary = cv2.threshold(gray , 200 ,255,cv2.THRESH_BINARY_INV)#反向阈值


kernel = np.ones((10,10),np.uint8)
#膨胀

erosion = cv2.erode(binary,kernel,10)

#腐蚀

dilation = cv2.dilate(binary,kernel,10)

"""
"""

kernel = np.ones((1,10),np.uint8)
#膨胀

erosion = cv2.erode(binary,kernel,10)

#腐蚀

dilation = cv2.dilate(binary,kernel,10)

"""



"""
cv2.imshow("binary",binary)
cv2.imshow("erosion ",erosion)
cv2.imshow("dilation ",dilation )
cv2.waitKey()
"""

"""
import cv2
import numpy as np
image = cv2.imread("9.png",cv2.COLOR_BGR2GRAY)

area = np.ones((10,10),np.uint8)

opimage = cv2.morphologyEx(image,cv2.MORPH_OPEN,area)
climage = cv2.morphologyEx(image,cv2.MORPH_CLOSE,area)


cv2.imshow("image",image)
cv2.imshow("opimage", opimage)
cv2.imshow("climage", climage)
cv2.waitKey()

"""

"""
开运算的作用：消除细小物体、在窄区域分离物体、平滑大物体边界等。

开运算函数： cv2.morphologyEx(图像, cv2.MORPH_OPEN,矩阵)

    cv2.MORPH_OPEN 是常量，意为开运算
    先膨胀后腐蚀的操作称为闭运算
作用：填充物体空洞、消除噪声、连接邻近物体、平滑边界等。

闭运算函数： cv2.morphologyEx(图像, cv2.MORPH_CLOSE,矩阵)

    cv2.MORPH_CLOSE 是常量，意为闭运算
"""

























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

# 显示结果
cv2.imshow('Original', image)
cv2.imshow('Canny Edges', edges)
cv2.waitKey()
