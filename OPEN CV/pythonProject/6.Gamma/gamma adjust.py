import cv2
import numpy as np
def Gammaadjust(image,gamma_point):
    temporaryimage = np.zeros_like(image)
    for i in range(len(image)):
        temporaryimage[i]=(image[i]/255.0)**(gamma_point)*255
    return temporaryimage


image = cv2.imread("6-2.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


gamma = 2.2
cv2.imshow("gray",gray)
gammaimage0 = Gammaadjust(gray,gamma)
cv2.imshow("gammaimage0",gammaimage0)
gammaimage1 = Gammaadjust(gray,0.5)
cv2.imshow("gammaimage1",gammaimage1)
cv2.waitKey()

