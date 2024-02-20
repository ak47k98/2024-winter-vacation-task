import cv2
image =cv2.imread("6-1.jpg")
gauss = cv2.GaussianBlur(image,(5,5),0)#高斯滤波器 ，内核设置为五个像素
cv2.imshow("image",image)
cv2.imshow("gauss",gauss)
cv2.waitKey()