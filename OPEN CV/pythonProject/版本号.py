import cv2
print(cv2.getVersionString())#版本号
image= cv2.imread("6-1.jpg")
print(image.shape)#打印维度(横行,竖行,三原色彩色通道)  BGR格式存储
cv2.imshow("image",image)
cv2.waitKey()#等待键盘输入，输入任意健消失    注意：K
