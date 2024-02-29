import cv2
image = cv2.imread("配图2.jpg")
print(image.shape)#打印维度(横行,竖行,三原色彩色通道)  BGR格式存储
cv2.imshow("blue",image[:,:, 0])
cv2.imshow("green",image[:,:, 1])
cv2.imshow("red",image[:,:, 2])
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#对BGR三原色 各灰度值进行加权平均   灰度图
cv2.imshow("gray",gray)
cv2.waitKey()
"""
import cv2 as cv
import numpy as np

def split_demo():
  img = cv.imread('./images/butterfly.jpg')
  cv.imshow('butterfly', img)
  b,g,r = cv.split(img)
  like_img_b = np.zeros_like(img)
  like_img_b[:,:,0] = b
  like_img_g = np.zeros_like(img)
  like_img_g[:,:,1] = g
  like_img_r = np.zeros_like(img)
  like_img_r[:,:,2] = r
  cv.imshow('butterfly_b', like_img_b)
  cv.imshow('butterfly_g', like_img_g)
  cv.imshow('butterfly_r', like_img_r)

  cv.waitKey(0)
  cv.destroyAllWindows()

if __name__ == "__main__":
  split_demo()

————————————————

                            版权声明：本文为博主原创文章，遵循 CC 4.0 BY 版权协议，转载请附上原文出处链接和本声明。

原文链接：https://blog.csdn.net/m0_38082783/article/details/127384118

`np.zeros_like` 是 NumPy 中的一个函数，用于创建一个与输入数组具有相同形状（shape）和数据类型（dtype），但所有元素都初始化为零的新数组。

具体使用方法如下：

```python
import numpy as np

# 创建一个示例数组
original_array = np.array([[1, 2, 3], [4, 5, 6]])

# 使用 np.zeros_like 创建与输入数组形状相同的零数组
zero_array = np.zeros_like(original_array)

# 打印结果
print("Original Array:")
print(original_array)

print("\nZero Array (same shape as original, but filled with zeros):")
print(zero_array)
```

在这个例子中，`zero_array` 将具有与 `original_array` 相同的形状，但所有元素都将初始化为零。

如果有其他问题或需要更多解释，请告诉我！
"""
