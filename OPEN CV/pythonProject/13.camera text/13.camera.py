import cv2


cap = cv2.VideoCapture(0)

#video="http://admin:admin@192.168.202.62:4747/video"      #更改ip

#cap =cv2.VideoCapture(video)










while True :
    success,img = cap.read()
    #gauss = cv2.GaussianBlur(img, (7, 7), 0)  # 高斯滤波器 ，内核设置为五个像素   #奇数
    median = cv2.medianBlur(img, 5)  # 中值滤波器
    imgCanny = cv2.Canny(img, 80, 160)
    # 均值滤波
    img_blur = cv2.blur(img, (5, 5))
    FPS=cap.get(cv2.CAP_PROP_FPS)
    print(FPS)

    cv2.imshow("video", img)
    cv2.imshow("canny",imgCanny)




    if cv2.waitKey(1) & 0xFF ==ord('q'):   #按q退出
        break