import cv2
import numpy as np
def freesize(image):
    # 获取图像原始大小
    height, width, _ = image.shape

    # 设定新的输出大小
    new_width = 200  # 替换为你想要的新宽度
    new_height = int((new_width / width) * height)

    # 改变输出图像大小
    resized_img = cv2.resize(image, (new_width, new_height))

    # 创建一个新的窗口
    cv2.namedWindow("Resized Image", cv2.WINDOW_NORMAL)

    # 在显示器的四个角显示图像
    cv2.imshow("Resized Image", resized_img)
    cv2.moveWindow("Resized Image", 0, 0)

image = np.zeros([300,300,3],dtype=np.uint8)#数据类型为无符号八位整数

cv2.line(image,(100,200),(250,250),(255,0,0),2)#直线 起点坐标 终点坐标 BGR颜色 粗细（几个像素）
cv2.rectangle(image,(30,100),(60,150),(0,255,0),2)#矩形
cv2.circle(image,(150,100),20,(0,0,255),2)#圆环
cv2.putText(image,"hello",(100,50),0,1,(255,255,255),2,1)#字体序号，缩放系数,,,线条类型

freesize(image)

cv2.waitKey()