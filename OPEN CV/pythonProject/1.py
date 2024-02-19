import cv2              #导入OpenCV库,opencv读取的格式是BGR
import matplotlib.pyplot as plt   #导入`matplotlib`库的`pyplot`模块，用于显示图像
import numpy as np      #导入NumPy库
img=cv2.imread('/home/ak47k98/populay/2024-winter-vacation-task/OPEN CV/photo/6-1.jpg')     #这一行使用OpenCV的`imread`函数读取名为'example.jpg'的图像文件，并将图像数据存储在变量`img`中
cv2.imshow("img",img)     #这一行使用OpenCV的`imshow`函数显示图像。第一个参数是窗口名称，第二个参数是图像数据
cv2.waitKey(0)           #此行等待按键事件。参数'0'表示它将无限期地等待，直到按下任意键
cv2.destroyAllWindows()   #在按下键并退出等待状态后，此行关闭所有OpenCV窗口