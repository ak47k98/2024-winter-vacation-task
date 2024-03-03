import cv2
import numpy as np
gray = cv2.imread("11.png",cv2.COLOR_BGR2GRAY)


# 使用Canny函数进行边缘检测
edges = cv2.Canny(gray, 100, 200)

"""
连通域

图像的连通域是指图像中具有相同像素值并且位置相邻的像素组成的区域，连通域分析是指在图像中寻找出彼此互相独立的连通域并将其标记出来。提取图像中不同的连通域是图像处理中较为常用的方法，在目标检测等领域对感兴趣区域分割与识别。- 般情况下，一个连通域内包含一个像素值。因此为了防止像素值波动对提取不同连通域的影响。连通域分析常处理的是二值化后的图像en

在了解图像连通域分析方法之前、首先需要了解图像邻域的概念。图像中两个像素相邻有两种定义方式分别是4:邻域和8-邻域en


OpenCV-python自带了连通域函数，如下:以下的标记方法只为了解原理。

cv2.connectedComponents (image, labels=None, connectivity=None, Itype=None)

Cv2 connectedComponentsWithAlgorithm (image, connectivity, ltype, ccltype, labels=None)

cv2.connectedComponentsWithStats (image, labels=None, stats=None, centroids=None, connectivity=None, ltype=None)

cv2.connectedComponentsWithStatsithAlgorithm (image, connectity, Itype, ccltype, labels=None, stats=None, centroids=None)

参数详解:

image :待标记不同连通域的单通道图像，数据类型必须为CV_ _8U。labels :标记不同连通域后的输出图像，与输入图像具有相同的尺寸。

connectivity :标记连通域时使用的邻域种类，4表示4 -邻域，8表示8- 邻域。tpe :输出图像的数据类型，目前支持CV_ _32S和CV_ 16U两种数据类型。cltype :标记连通域时使用的算法类型标志，可以选择的参数下表中给出。

"""

median = cv2.medianBlur(gray,5)  # 中值滤波，去噪

# 阈值分割得到二值化图片
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)





cv2.imshow("image",gray)
cv2.imshow("edges",edges)
cv2.waitKey()