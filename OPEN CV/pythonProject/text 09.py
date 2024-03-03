import cv2
import numpy as np
gray = cv2.imread("9.png",cv2.IMREAD_GRAYSCALE)
ret,binary = cv2.threshold(gray , 200 ,255,cv2.THRESH_BINARY_INV)#反向阈值


#腐蚀
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(binary,kernel)


#膨胀
dilation = cv2.dilate(binary,kernel)


















cv2.imshow("binary",binary)
cv2.imshow("erosion ",erosion)
cv2.imshow("dilation ",dilation )
cv2.waitKey()
