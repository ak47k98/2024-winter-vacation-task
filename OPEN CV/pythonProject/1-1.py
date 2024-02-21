import cv2
import numpy as np

# 读取图像
img = cv2.imread('/home/ak47k98/populay/2024-winter-vacation-task/OPEN CV/photo/6-1.jpg')

# 获取图像原始大小
height, width, _ = img.shape

# 设定新的输出大小
new_width = 200  # 替换为你想要的新宽度
new_height = int((new_width / width) * height)

# 改变输出图像大小
resized_img = cv2.resize(img, (new_width, new_height))

# 创建一个新的窗口
cv2.namedWindow("Resized Image", cv2.WINDOW_NORMAL)0

# 在显示器的四个角显示图像
cv2.imshow("Resized Image", resized_img)
cv2.moveWindow("Resized Image", 0, 0)

cv2.waitKey(0)
cv2.destroyAllWindows()