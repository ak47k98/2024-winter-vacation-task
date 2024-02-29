"""
import cv2
def freesize(image):
    # 获取图像原始大小
    height, width, _ = image.shape

    # 设定新的输出大小
    new_width = 200  # 替换为你想要的新宽度
    new_height = int((new_width / width) * height)

    # 改变输出图像大小
    resized_img = cv2.resize(image, (new_width, new_height))

    # 创建一个新的窗口
    cv2.namedWindow("Resized Image", cv2.WINDOW_NORMAL)

    # 在显示器的四个角显示图像
    cv2.imshow("Resized Image", resized_img)
    cv2.moveWindow("Resized Image", 0, 0)
"""