"""
event 具体说明如下：

EVENT_MOUSEMOVE 0 //滑动
EVENT_LBUTTONDOWN 1 //左键点击
EVENT_RBUTTONDOWN 2 //右键点击
EVENT_MBUTTONDOWN 3 //中键点击
EVENT_LBUTTONUP 4 //左键放开
EVENT_RBUTTONUP 5 //右键放开
EVENT_MBUTTONUP 6 //中键放开
EVENT_LBUTTONDBLCLK 7 //左键双击
EVENT_RBUTTONDBLCLK 8 //右键双击
EVENT_MBUTTONDBLCLK 9 //中键双击
flags 具体说明如下：

EVENT_FLAG_LBUTTON 1 //左键拖曳
EVENT_FLAG_RBUTTON 2 //右键拖曳
EVENT_FLAG_MBUTTON 4 //中键拖曳
EVENT_FLAG_CTRLKEY 8 //(8~15)按 Ctrl 不放
EVENT_FLAG_SHIFTKEY 16 //(16~31)按 Shift 不放
EVENT_FLAG_ALTKEY 32 //(32~39)按 Alt 不放


"""




import cv2
import numpy as np



def mouse_callback_color(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("position is :", x, y)
        print("blue:",image[x,y,0],"green:",image[x,y,1],"red:",image[x,y,2])

image=cv2.imread("3.png")




cv2.imshow("image",image)
cv2.setMouseCallback("image",mouse_callback_color)
cv2.waitKey()