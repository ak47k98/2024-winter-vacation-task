import cv2
import numpy as np
img = cv2.imread ("12.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret , gray = cv2.threshold(gray,100,255,cv2.THRESH_OTSU)
resover = cv2.bitwise_not(gray)
cv2.imshow("resover",resover)



num_labels , labels , stats , centroids = cv2.connectedComponentsWithStats(resover,8)
number = 0
output = img.copy()
contours , hierarchy = cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for stat in stats[1:] :
    if int(stat[ cv2.CC_STAT_AREA])>=2000 and int(stat[cv2.CC_STAT_AREA])<=8000  :
        number+=1
        cv2.rectangle(output,
                      (stat[cv2.CC_STAT_LEFT], stat[cv2.CC_STAT_TOP]),
                      (stat[cv2.CC_STAT_LEFT] + stat[cv2.CC_STAT_WIDTH],
                       stat[cv2.CC_STAT_TOP] + stat[cv2.CC_STAT_HEIGHT]),
                      (0, 255, 0), 3)
for contour in contours :
    if cv2.contourArea(contour)>=2000 and cv2.contourArea(contour)<=8000 :
        cv2.drawContours(output,[contour],0,(0,0,255),2)
        hull = cv2.convexHull(contour)
        cv2.drawContours(output,[hull],-1,(255,0,0),2)

print('number = ',number)
cv2.imshow("result",output)













cv2.waitKey()
