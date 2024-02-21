import cv2
image = cv2.imread("配图2.jpg")
print(image.shape)#打印维度(横行,竖行,三原色彩色通道)  BGR格式存储
cv2.imshow("blue",image[:,:, 0])
cv2.imshow("green",image[:,:, 1])
cv2.imshow("red",image[:,:, 2])
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#对BGR三原色 各灰度值进行加权平均   灰度图
cv2.imshow("gray && average &&  BGR",gray)
cv2.waitKey() 