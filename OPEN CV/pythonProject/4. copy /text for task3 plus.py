import cv2
import copy
image0 = cv2.imread("3.png")
image1 = copy.copy(image0)
image2 = copy.deepcopy(image0)
gray1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)#对BGR三原色 各灰度值进行加权平均
gray2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)#对BGR三原色 各灰度值进行加权平均



avevalue = 127
avevalue,result1=cv2.threshold(gray1,avevalue,255,cv2.THRESH_BINARY)
avevalue,result2=cv2.threshold(gray2,avevalue,255,cv2.THRESH_BINARY)
cv2.imshow("result1",result1)
cv2.imshow("result2",result2)
cv2.waitKey()
"""在使用函数之前，不用开辟内存。该函数会自己开一段内存，然后复制好图像里面的数据，然后返回这段内存中的数据。clone是把所有的都复制过来，不论你是否设置了ROI、COI等影响，clone都会原封不动的克隆过来。用clone复制后，如果源图像在内存中消失，复制的图像也变了，而用copy复制，源图像消失后，复制的图像不变。
————————————————

                            版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。
                        
原文链接：https://blog.csdn.net/zqx951102/article/details/83150635"""