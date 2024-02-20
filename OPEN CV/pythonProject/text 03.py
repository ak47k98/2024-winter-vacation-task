import cv2
image = cv2.imread("配图2.jpg")
print(image.shape)
crop = image [10:400,40:200]#裁剪图片，先纵列再横行  从10到170  ，从40到200
cv2.imshow("crop",crop)
cv2.waitKey()