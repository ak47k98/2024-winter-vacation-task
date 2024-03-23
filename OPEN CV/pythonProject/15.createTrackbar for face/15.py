
"""

cv2.createTrackbar(“scale”, “display”, 0, 100, self.opencv_calibration_node.on_scale)

功能：
绑定滑动条和窗口，定义滚动条的数值

参数
第一个参数时滑动条的名字，
第二个参数是滑动条被放置的窗口的名字，
第三个参数是滑动条默认值，
第四个参数时滑动条的最大值，
第五个参数时回调函数，每次滑动都会调用回调函数。



函数getTrackbarPos：
cv2.getTrackbarPos()

功能：
得到滑动条的数值

参数
第一个参数是滑动条名字，
第二个时所在窗口，
返回值是滑动条的数值。


函数setTrackbarPos：
cv2.setTrackbarPos(‘Alpha’, ‘image’, 100)

功能：
设置滑动条的默认值

参数
第一个参数是滑动条名字，
第二个时所在窗口，
第三个参数是滑动条默认值，


"""




"""
def nothing(pos):
    pass

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




"""


import cv2
import numpy as np
def nothing(x):
    pass

# 读取图像
img = cv2.imread("14-1.jpg")

# 创建窗口
cv2.namedWindow("Blur Parameters")


mean_val = cv2.mean(img)[0]
#_, otsu_thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 创建跟踪条，一个用于高斯模糊核大小，一个用于中值模糊核大小
cv2.createTrackbar("threshold size","Blur Parameters",int(mean_val),255,nothing)
cv2.createTrackbar("Gaussian Kernel Size", "Blur Parameters", 1, 30, nothing)
cv2.createTrackbar("Median Kernel Size", "Blur Parameters", 1, 30, nothing)
while(True):
    # 获取跟踪条的当前位置作为核大小
    gauss_size = cv2.getTrackbarPos("Gaussian Kernel Size", "Blur Parameters")
    median_size = cv2.getTrackbarPos("Median Kernel Size", "Blur Parameters")
    threshold_size = cv2.getTrackbarPos("threshold size","Blur Parameters")

    # 确保核大小为正奇数
    gauss_size = max(1, gauss_size)
    median_size = max(1, median_size)
    if gauss_size % 2 == 0:
        gauss_size += 1
    if median_size % 2 == 0:
        median_size += 1

    # 应用高斯滤波和中值滤波
    ret,image = cv2.threshold(img,threshold_size,255,cv2.THRESH_BINARY)
    gauss = cv2.GaussianBlur(image, (gauss_size, gauss_size), 0)
    median = cv2.medianBlur(gauss, median_size)
    gauss1 = cv2.GaussianBlur(img, (gauss_size, gauss_size), 0)
    median1 = cv2.medianBlur(gauss1, median_size)

    # 在窗口中显示结果
    cv2.imshow("threshold image",image)
    cv2.imshow("Gaussian Blurred", gauss)
    cv2.imshow("Median Blurred", median)
    cv2.imshow("Gaussian Blurred1", gauss1)
    cv2.imshow("Median Blurred1", median1)
    # 按 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 关闭所有窗口
cv2.destroyAllWindows()




