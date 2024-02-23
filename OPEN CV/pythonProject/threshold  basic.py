import cv2
import numpy as np
image=cv2.imread("3.png")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#对BGR三原色 各灰度值进行加权平均   灰度图

"""
使用语法：thresh,result=cv2.threshold (src(原图), thresh（阀值）, maxval（处理后的取高）, type)

参数说明：thresh为设定的阈值，取值范围即为灰度值的范围0~255，数据类型为浮点型（输入可以为整型）；

                  result为进行阈值分割后的结果图像，数据类型为整数矩阵；

                  src为被进行分割的源图像，一般为单通道的灰度图，但三通道的RGB图像也可以进行处理（但可能只根据第一个通道的大小进行处理（所谓枪打出头鸟））

                  maxval为最大值，为分割后的图像所取到的灰度最大值

                  type为阈值分割的类型，常用的有THRESH_BINARY、THRESH_BINARY_INV、THRESH_TOZERO、THRESH_TOZERO_INV。具体的说明可见下表所示：



thresh,result0=cv2.threshold(src,80,255,cv2.THRESH_BINARY)         #THRESH_BINARY	灰度值超过阈值的像素设置为最大灰度值，不超过的设置为0
thresh,result2=cv2.threshold(gray,80,255,cv2.THRESH_BINARY_INV)    #THRESH_BINARY_INV	灰度值不超过阈值的像素设置为最大灰度值，超过的设置为0   与前者效果相反
thresh,result3=cv2.threshold(gray,80,255,cv2.THRESH_TOZERO)        #THRESH_TOZERO	灰度值低于阀值的像素设为0灰度值
thresh,result4=cv2.threshold(gray,80,255,cv2.THRESH_TOZERO_INV)    #THRESH_TOZERO_INV	灰度值高于阀值的像素设为0灰度值   与前者效果相反
thresh,result5=cv2.threshold(gray,80,255,cv2.THRESH_TRUNC)         #THRESH_TRUNC	灰度值超过阈值的像素设为阈值的灰度值
                        
原文链接：https://blog.csdn.net/m0_55320151/article/details/127192801
————————————————————————————————————————————————————————————————
1. **`cv2.THRESH_MASK`**：
   - **解释：** 这个标志通常与掩码一起使用。掩码是一个与输入图像大小相同的矩阵，用于指定哪些像素应该参与阈值处理，哪些不应该。
   - **示例：**
     ```python
     ret, binary_result = cv2.threshold(image, thresh_value, 255, cv2.THRESH_BINARY + cv2.THRESH_MASK, mask)
     ```
     在这个示例中，`mask` 是一个与输入图像大小相同的矩阵，指定哪些像素参与阈值处理。

2. **`cv2.THRESH_OTSU`**：
   - **解释：** 使用大津算法来选择最佳阈值，该算法适用于具有双峰直方图的图像。只支持8位单通道图像。
   - **示例：**
     ```python
     ret, binary_result = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
     ```
     在这个示例中，阈值被设置为0，函数会使用大津算法来选择最佳阈值。

3. **`cv2.THRESH_TRIANGLE`**：
   - **解释：** 使用TRIANGLE算法来计算最佳阈值，同样适用于具有双峰直方图的图像。只支持8位单通道图像。
   - **示例：**
     ```python
     ret, binary_result = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_TRIANGLE)
     ```
     在这个示例中，阈值被设置为0，函数会使用TRIANGLE算法来计算最佳阈值。



————————————————————————————————————————————————————————————————
import cv2
import numpy as np

# 读取一张灰度图像
image = cv2.imread('your_image.jpg', cv2.IMREAD_GRAYSCALE)

# 设定阈值
thresh_value = 127

# 使用 cv2.threshold 进行二值化处理
# 返回两个值，第一个是实际使用的阈值，第二个是处理后的结果图像
ret, binary_result = cv2.threshold(image, thresh_value, 255, cv2.THRESH_BINARY)

# 显示原始图像和处理后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Binary Result', binary_result)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""