import cv2
import numpy as np

image = cv2.imread("12.png")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
crop = gray [30:215,60:240]#裁剪图片，先纵列再横行  从10到170  ，从40到200
"""
match =cv2.matchTemplate(gray,crop,cv2.TM_CCOEFF_NORMED)#待检测图像，模板，标准相关匹配算法（将两者各自标准化并计算匹配度）
locations = np.where(match>=0.9)#找出匹配系数大于0.9匹配点
w, h =crop.shape[0:2]     #求长和宽
for p in zip(*crop[::-1]):
    x1,y1=p[0],p[1]
    x2,y2 =x1+w,y1+h
    cv2.rectangle(image,(x1,y1),(x2,y2),(0,255,0))

cv2.imshow("image",image)
cv2.waitKey()
"""



cv2.imshow("crop",crop)
cv2.waitKey()

