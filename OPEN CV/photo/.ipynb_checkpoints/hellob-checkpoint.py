import cv2 #opencv读取的格式是BGR
import matplotlib.pyplot as plt
import numpy as np 
%matplotlib inline 
img=cv2.imread('6-1.jpg')
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
