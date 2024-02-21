import cv2
image =cv2.imread("14-1.jpg")
gauss = cv2.GaussianBlur(image,(7,7),0)#高斯滤波器 ，内核设置为五个像素   #奇数
median = cv2.medianBlur(image,5) #中值滤波器
imgCanny = cv2.Canny(image,150,200)
"""
cv2.Canny()函数是OpenCV中用于边缘检测的函数，其主要功能是检测图像中的边缘并标记出来。
函数的调用格式如下：
edges = cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]])
其中，参数含义如下：
    image：要进行边缘检测的输入图像，可以是灰度图像或彩色图像。
    threshold1：第一个阈值，用于边缘检测中的滞后阈值，建议取值为100。
    threshold2：第二个阈值，用于边缘检测中的滞后阈值，建议取值为200。
    edges：可选参数，用于存储边缘检测的结果。如果指定了该参数，则该参数会被用来存储检测到的边缘图像。如果没有指定该参数，则函数会自动创建一个与输入图像相同大小的数组来存储检测到的边缘图像。
    apertureSize：可选参数，用于指定Sobel算子的大小，建议取值为3。
    L2gradient：可选参数，用于指定是否使用 L 2 L_2 L2​梯度计算方式。默认值为False，表示使用 L 1 L_1 L1​梯度计算方式。
"""
cv2.imshow("image",image)
cv2.imshow("gauss",gauss)
cv2.imshow("median",median)
cv2.imshow("Canny",imgCanny)
cv2.waitKey()
