"""
import cv2
img = cv2.imread("14-1.jpg")
# 获取和修改像素值
px = img[100,100]
print(px)

# 修改像素值
img[100,100] = [255,255,255]
print(img[100,100])

# 获取图像属性
print(img.shape)
print(img.size)
print(img.dtype)

# 设置ROI
roi = img[100:200, 100:200]

# 拆分和合并图像通道
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))



# 转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 转换为HSV图像
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

import cv2
import numpy as np

# 载入图像并转为灰度图
img = cv2.imread('image.jpg',0)

# 阈值化处理
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# 显示处理结果
cv2.imshow('threshold',thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()
当使用 `cv2.threshold` 函数时，以下是一个简单的例子，假设你有一张灰度图像 `gray_image`：

```python
import cv2

# 读取灰度图像
gray_image = cv2.imread('your_image.jpg', cv2.IMREAD_GRAYSCALE)

# 设定阈值
thresh_value = 127

# 使用 cv2.threshold 进行二值化处理
thresh, binary_result = cv2.threshold(gray_image, thresh_value, 255, cv2.THRESH_BINARY)

# 显示原始图像和处理后的图像
cv2.imshow('Original Image', gray_image)
cv2.imshow('Binary Result', binary_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

在这个例子中，`thresh_value` 被设定为 127，即阈值。`cv2.THRESH_BINARY` 被用于二值化处理，其中大于阈值的像素值被设置为255，小于等于阈值的像素值被设置为0。处理后的图像将显示在窗口中。

记得替换 `'your_image.jpg'` 为实际的图像文件路径。这个例子展示了如何对图像进行二值化处理，根据阈值将像素分为两个类别。    """
