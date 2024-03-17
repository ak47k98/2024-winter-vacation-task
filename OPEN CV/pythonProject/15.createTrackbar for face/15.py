import cv2
import numpy as np
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


# 回调函数，用于跟踪条的相应操作，本例中不需要实际操作
def nothing(x):
    pass

# 读取图像
img = cv2.imread("14-1.jpg")

# 创建窗口
cv2.namedWindow("Blur Parameters")

# 创建跟踪条，一个用于高斯模糊核大小，一个用于中值模糊核大小
cv2.createTrackbar("Gaussian Kernel Size", "Blur Parameters", 1, 30, nothing)
cv2.createTrackbar("Median Kernel Size", "Blur Parameters", 1, 30, nothing)

while(True):
    # 获取跟踪条的当前位置作为核大小
    gauss_size = cv2.getTrackbarPos("Gaussian Kernel Size", "Blur Parameters")
    median_size = cv2.getTrackbarPos("Median Kernel Size", "Blur Parameters")

    # 确保核大小为正奇数
    gauss_size = max(1, gauss_size)
    median_size = max(1, median_size)
    if gauss_size % 2 == 0:
        gauss_size += 1
    if median_size % 2 == 0:
        median_size += 1

    # 应用高斯滤波和中值滤波
    gauss = cv2.GaussianBlur(img, (gauss_size, gauss_size), 0)
    median = cv2.medianBlur(gauss, median_size)

    # 在窗口中显示结果
    cv2.imshow("Gaussian Blurred", gauss)
    cv2.imshow("Median Blurred", median)

    # 按 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 关闭所有窗口
cv2.destroyAllWindows()