import cv2
import numpy as np
gray = cv2.imread("9.png",cv2.IMREAD_GRAYSCALE)
ret,binary = cv2.threshold(gray , 200 ,255,cv2.THRESH_BINARY_INV)#反向阈值


kernel = np.ones((10,10),np.uint8)
#膨胀

erosion = cv2.erode(binary,kernel,10)

#腐蚀

dilation = cv2.dilate(binary,kernel,10)


"""

kernel = np.ones((1,10),np.uint8)


#膨胀

erosion = cv2.erode(binary,kernel,10)

#腐蚀

dilation = cv2.dilate(binary,kernel,10)

"""




cv2.imshow("binary",binary)
cv2.imshow("erosion ",erosion)
cv2.imshow("dilation ",dilation )
cv2.waitKey()
