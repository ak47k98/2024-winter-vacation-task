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

开运算的作用：消除细小物体、在窄区域分离物体、平滑大物体边界等。

开运算函数： cv2.morphologyEx(图像, cv2.MORPH_OPEN,矩阵)

    cv2.MORPH_OPEN 是常量，意为开运算
    先膨胀后腐蚀的操作称为闭运算
作用：填充物体空洞、消除噪声、连接邻近物体、平滑边界等。

闭运算函数： cv2.morphologyEx(图像, cv2.MORPH_CLOSE,矩阵)

    cv2.MORPH_CLOSE 是常量，意为闭运算

"""