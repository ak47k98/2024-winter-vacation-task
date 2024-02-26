import cv2
import copy
image0 = cv2.imread("3.png")
image1 = copy.copy(image0)
image2 = copy.deepcopy(image0)
gray1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)#对BGR三原色 各灰度值进行加权平均
gray2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)#对BGR三原色 各灰度值进行加权平均



avevalue = 127
avevalue,result1=cv2.threshold(gray1,avevalue,255,cv2.THRESH_BINARY)
avevalue,result2=cv2.threshold(gray2,avevalue,255,cv2.THRESH_BINARY)
cv2.imshow("result1",result1)
cv2.imshow("result2",result2)
cv2.waitKey()