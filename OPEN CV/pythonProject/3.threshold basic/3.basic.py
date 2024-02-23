import cv2
import numpy as np
image=cv2.imread("3.png")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#对BGR三原色 各灰度值进行加权平均

avevalue = 127
avevalue,result0=cv2.threshold(gray,avevalue,255,cv2.THRESH_BINARY)
avevalue = 240
avevalue,result1=cv2.threshold(gray,avevalue,255,cv2.THRESH_BINARY)
avevalue,result2=cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)

avevalue,result3=cv2.threshold(gray,127,255,cv2.THRESH_TOZERO)




avevalue,result4= cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


cv2.imshow("result0",result0)
cv2.imshow("result1",result1)
cv2.imshow("result2",result2)
cv2.imshow("result3",result3)
cv2.imshow("result4",result4)
cv2.imshow("gray",gray)
cv2.waitKey()