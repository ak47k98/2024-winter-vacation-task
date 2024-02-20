import cv2
import numpy as np
image = np.zeros([300,300,3],dtype=np.uint8)#数据类型为无符号八位整数

cv2.line(image,(100,200),(250,250),(255,0,0),2)#直线 起点坐标 终点坐标 BGR颜色 粗细（几个像素）
cv2.rectangle(image,(30,100),(60,150),(0,255,0),2)#矩形
cv2.circle(image,(150,100),20,(0,0,255),2)#圆环
cv2.putText(image,"hello",(100,50),0,1,(255,255,255),2,1)#字体序号，缩放系数,,,线条类型

cv2.imshow("image",image)
cv2.waitKey()