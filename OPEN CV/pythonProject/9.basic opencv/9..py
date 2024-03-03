
import cv2
import numpy as np
image = cv2.imread("9.png",cv2.COLOR_BGR2GRAY)

area = np.ones((10,10),np.uint8)

opimage = cv2.morphologyEx(image,cv2.MORPH_OPEN,area)
climage = cv2.morphologyEx(image,cv2.MORPH_CLOSE,area)


cv2.imshow("image",image)
cv2.imshow("opimage", opimage)
cv2.imshow("climage", climage)
cv2.waitKey()

