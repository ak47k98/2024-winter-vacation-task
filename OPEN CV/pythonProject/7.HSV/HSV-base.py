import cv2


image = cv2.imread('配图2.jpg')
cv2.imshow('image', image)
dst = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('image_hsv', dst)
b, g, r = cv2.split(dst)
cv2.imshow('image_b', b)
cv2.imshow('image_g', g)
cv2.imshow('image_r', r)

cv2.waitKey()
