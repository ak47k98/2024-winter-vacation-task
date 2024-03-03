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



"""
rgb 221,0,27 可以转换成 hsv 的格式，具体的方法如下：
 
首先，我们需要将 rgb 值转换成浮点数，方法是将每个值除以 255。因此，rgb(221,0,27) 可以转换成 (0.8666666666666667, 0.0, 0.10588235294117647)。
 
然后，我们可以使用以下公式来计算 hsv 值：
 
h = 色相，s = 饱和度，v = 明度
 
maxc = max(r, g, b)
minc = min(r, g, b)
 
if maxc == minc:
h = 0
elif maxc == r:
h = 60 * ((g - b) / (maxc - minc))
elif maxc == g:
h = 60 * (2 + (b - r) / (maxc - minc))
else:
h = 60 * (4 + (r - g) / (maxc - minc))
 
if h < 0:
h += 360
 
s = 0 if maxc == 0 else (1 - minc / maxc)
v = maxc
 
所以，rgb(221,0,27) 可以转换成 hsv(348.57142857142856, 1.0, 0.8666666666666667)。
 
注意：在计算 hsv 值时，色相 h 的单位是角度，饱和度 s 和明度 v 的单位都是百分比，它们的取值范围分别是 0 到 360、0 到 1 和 0 到 1。

tool : https://www.jyshare.com/front-end/868/
"""
"""
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('配图2.jpg')
 
    # 从RGB色彩空间转换到HSV色彩空间
hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
 
    # 颜色范围下限
lower_threshold = np.array([110, 254, 220])
    # 颜色范围上限
upper_threshold = np.array([180, 255, 255])
 
    # 使用inRange函数检测颜色
mask = cv2.inRange(hsv, lower_threshold, upper_threshold)
 
    # 对原图像和掩码进行位运算
result = cv2.bitwise_and(image, image, mask=mask)
 
    # H、S、V范围二：
cv2.imshow("result", mask)
cv2.imshow("image", image)
 
cv2.waitKey()
cv2.destroyAllWindows()
    
    
    
    
    
    # 颜色范围下限red
lower_threshold = np.array([0, 255, 255])
    # 颜色范围上限
upper_threshold = np.array([180, 255, 255])
    #V亮度调整
    # 颜色范围下限
lower_threshold = np.array([0, 255, 200])
    # 颜色范围上限
upper_threshold = np.array([180, 255, 255])
    
    # 颜色范围下限
lower_threshold = np.array([0, 254, 200])
    # 颜色范围上限
upper_threshold = np.array([180, 255, 255])
    
        # 颜色范围下限
lower_threshold = np.array([120, 254, 200])
    # 颜色范围上限
upper_threshold = np.array([180, 255, 255])
    
    
    
    
        # 颜色范围下限    210     blue
lower_threshold = np.array([10, 210, 255])
    # 颜色范围上限
upper_threshold = np.array([20, 215, 255])
"""
"""
import cv2

image = cv2.imread('配图2.jpg')
cv2.imshow('image', image)
dst = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('image_hsv', dst)
b, g, r = cv2.split(dst)
cv2.imshow('image_b', b)
cv2.imshow('image_g', g)
cv2.imshow('image_r', r)

cv2.waitKey()"
"""
"""
inRange()函数

      OpenCV中的inRange()函数可实现二值化功能（这点类似threshold()函数），更关键的是可以同时针对多通道进行操作，使用起来非常方便！主要是将在两个阈值内的像素值设置为白色（255），而不在阈值区间内的像素值设置为黑色（0），该功能类似于之间所讲的双阈值化操作。
      官方文档中的解释：Checks if array elements lie between the elements of two other arrays.即检查数组元素是否在另外两个数组元素值之间。这里的数组通常也就是矩阵Mat或向量。请注意：该函数输出的dst是一幅二值化之后的图像


"""