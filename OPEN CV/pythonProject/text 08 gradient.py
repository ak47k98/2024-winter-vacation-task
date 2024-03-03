import cv2

gary = cv2.imread("14-1.jpg",cv2.IMREAD_GRAYSCALE)

laplacian = cv2.Laplacian(gary,cv2.CV_64F)    #拉普拉斯算子  表示图像的二阶导数

canny = cv2.Canny(gary,100,200)#图像，确认不是边缘，确认是边缘

cv2.imshow("gary",gary)
cv2.imshow("laplacian",laplacian)
cv2.imshow("canny",canny)
cv2.waitKey()