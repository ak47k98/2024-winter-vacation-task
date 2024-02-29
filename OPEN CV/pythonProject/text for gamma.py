import cv2
import numpy as np
def Gammaadjust(image,gamma_point):
    temporaryimage = np.zeros_like(image)
    for i in range(len(image)):
        temporaryimage[i]=(image[i]/255.0)**(gamma_point)*255
    return temporaryimage


image = cv2.imread("6-1.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
"""
    归一化：将像素值从原始范围（如0至255）转换到一个新的范围（0至1）。这是通过除以最大值 \( 255/256 \) 和加上0.5得到的。

    预补偿：计算归一化像素值以\( 1/\gamma \)为指数的对应值。这涉及到一个指数运算。例如，如果\( \gamma = 2.2 \)，则计算过程是将归一化的像素值\[ \frac{i+0.5}{256} \]向上取整并乘以\( 2.2^{-1} \)。

    反归一化：将经过预补偿的实数值反变换回原始的0至255整数范围内。这涉及两个操作：乘256然后减去0.5。
"""
gamma = 2.2
cv2.imshow("gray",gray)
gammaimage0 = Gammaadjust(gray,gamma)
cv2.imshow("gammaimage0",gammaimage0)
gammaimage1 = Gammaadjust(gray,0.5)
cv2.imshow("gammaimage1",gammaimage1)
cv2.waitKey()


