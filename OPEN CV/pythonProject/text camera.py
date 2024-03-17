import cv2
cap = cv2.VideoCapture(0)    #调用默认摄像头
cap.set(cv2.CAP_PROP_FPS, 30)#设置帧率为30
#cap.set(3,640)    #设置尺寸  宽度
#cap.set(4,480)    #高度
cap.set (10,100)#亮度   11对比度
while True :
    success,img=cap.read()
    median = cv2.medianBlur(img, 5)  # 中值滤波器



    cv2.imshow("video", img)
    cv2.imshow("video1", median)
    if cv2.waitKey(1) & 0xFF ==ord('q'):   #按q退出
        break
"""
0	cv2.CAP_PROP_POS_MSEC	视频文件的当前位置(ms)
1	cv2.CAP_PROP_POS_FRAMES	从0开始索引帧，帧位置
2	cv2.CAP_PROP_POS_AVI_RATIO	视频文件的相对位置(0表示开始，1表示结束)
3	cv2.CAP_PROP_FRAME_WIDTH	视频流的帧宽度
4	cv2.CAP_PROP_FRAME_HEIGHT	视频流的帧高度
5	cv2.CAP_PROP_FPS	帧率
6	cv2.CAP_PROP_FOURCC	编解码器四字符代码
7	cv2.CAP_PROP_FRAME_COUNT	视频文件的帧
"""
