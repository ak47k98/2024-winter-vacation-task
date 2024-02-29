"""
HSV模型： 而HSV模型，是针对用户观感的一种颜色模型，侧重于色彩表示，什么颜色、深浅度、明暗度。

色调（H），饱和度（S），明度（V）

    H：Hue即色相，就是我们平时所说的红、绿，如果你分的更细的话可能还会有洋红、草绿等等；在HSV模型中，用度数来描述色相，其中红色对应0度，绿色对应120度，蓝色对应240度。
    S：Saturation即饱和度，色彩的深浅度(0-100%) ，对于一种颜色比如红色，我们可以用浅红——大红——深红——红得发紫等等语言来描述它（请原谅一个纯理科生的匮乏的颜色系统），对应在画水彩的时候即一种颜料加上不同分量的水形成不同的饱和度。
    V：Value即色调，纯度，色彩的亮度(0-100%) ，这个在调整屏幕亮度的时候比较常见。


    需要注意的是在OpenCV中 HSV的取值范围分别是 H:(0-180)，S:(0-255)，V:(0-255)。

————————————————

                            版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。

原文链接：https://blog.csdn.net/m0_48300767/article/details/125849400
"""
import cv2
import numpy as np


def nothing(x):
    pass


# 通过Opencv读取图片信息
# src = cv2.imread('image.jpg')
img = cv2.imread('配图2.jpg')
rows, cols, channels = img.shape
cv2.imshow("src", img)
cv2.namedWindow('img2', 1)
# cv2.resizeWindow("img2", 400, 200) #创建一个500*500大小的窗口

# 创建6个滑条用来操作HSV3个分量的上下截取界限
cv2.createTrackbar('Hlow', 'img2', 62, 180, nothing)
cv2.createTrackbar('Hup', 'img2', 99, 180, nothing)
cv2.createTrackbar('Slow', 'img2', 198, 255, nothing)
cv2.createTrackbar('Sup', 'img2', 255, 255, nothing)
cv2.createTrackbar('Vlow', 'img2', 150, 255, nothing)
cv2.createTrackbar('Vup', 'img2', 255, 255, nothing)

# lower_red = np.array([55,30,30])
# upper_red = np.array([99,255,255])
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
while (1):
    # mask = cv2.inRange(hsv, lower_red, upper_red)
    # 将制定像素点的数据设置为0, 要注意的是这三个参数对应的值是Blue, Green, Red。
    hlow = cv2.getTrackbarPos('Hlow', 'img2')
    hup = cv2.getTrackbarPos('Hup', 'img2')
    slow = cv2.getTrackbarPos('Slow', 'img2')
    sup = cv2.getTrackbarPos('Sup', 'img2')
    vlow = cv2.getTrackbarPos('Vlow', 'img2')
    vup = cv2.getTrackbarPos('Vup', 'img2')
    lower_red = np.array([hlow, slow, vlow])
    upper_red = np.array([hup, sup, vup])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    img2 = cv2.bitwise_and(img, img, mask=mask)

    # cv2.imshow("src", src)
    cv2.imshow("img2", img2)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # esc exit
        break
# cv2.waitKey(0)
