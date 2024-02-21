import cv2
image = cv2.imread("14-1.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#转化为灰度图

median = cv2.medianBlur(gray,5) #中值滤波器
corners = cv2.goodFeaturesToTrack(median,500,0.1,10)#获取图像中的特征点,最多返回500个点，点的质量为0.1，点之间的距离不少于10个像素

for corner in corners:
    x, y = corner.ravel()  #返回一个展平的数组  浮点数
    cv2.circle(image,(int(x),int(y)),3,(255,0,255),-1)

cv2.imshow("corners",image)

corners2 = cv2.goodFeaturesToTrack(gray,500,0.1,10)#获取图像中的特征点,最多返回500个点，点的质量为0.1，点之间的距离不少于10个像素

for corner in corners2:
    x, y = corner.ravel()  #返回一个展平的数组  浮点数
    cv2.circle(image,(int(x),int(y)),3,(255,0,255),-1)

cv2.imshow("corners2",image)
cv2.waitKey()
