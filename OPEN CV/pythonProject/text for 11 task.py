import cv2
import numpy as np

# 读入图片
img = cv2.imread("11.png")





# 中值滤波，去噪
img = cv2.medianBlur(img, 5)
img = cv2.GaussianBlur(img,(7,7),0)




gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.namedWindow('original', cv2.WINDOW_AUTOSIZE)
#cv2.imshow('original', gray)





"""
# 阈值分割得到二值化图片
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
"""
ret, binary=cv2.threshold(gray,85,255,cv2.THRESH_BINARY)
"""

binary = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,155,1)


binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
"""


"""
# 膨胀操作
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
bin_clo = cv2.dilate(binary, kernel2, iterations=2)
"""


#cv2.imshow('original', binary)
binary=cv2.morphologyEx(binary, cv2.MORPH_OPEN,(8,8))
binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE,(8,8))



#edges = cv2.Canny(binary, 100, 200)


# 连通域分析
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary, connectivity=8)



"""
# 查看各个返回值
# 连通域数量
print('num_labels = ', num_labels)
# 连通域的信息：对应各个轮廓的x、y、width、height和面积
print('stats = ', stats)
# 连通域的中心点
print('centroids = ', centroids)
# 每一个像素的标签1、2、3.。。，同一个连通域的标签是一致的
print('labels = ', labels)

# 不同的连通域赋予不同的颜色
output = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
for i in range(1, num_labels):
    mask = labels == i
    output[:, :, 0][mask] = np.random.randint(0, 255)
    output[:, :, 1][mask] = np.random.randint(0, 255)
    output[:, :, 2][mask] = np.random.randint(0, 255)
cv2.imshow('final', output)
cv2.waitKey()
cv2.destroyAllWindows()
"""

# 定义颜色映射
colors = [(255, 255, 255)] # 背景颜色
for i in range(1, num_labels):
    colors.append((int(centroids[i][0]+20) % 256, int(centroids[i][1]+50) % 256, i % 256))

# 创建输出图像用于标记连通域，并筛选出大小合适的连通域
output = np.zeros((gray.shape[0], gray.shape[1], 3), np.uint8)
min_size = 100  # 设定最小连通域的大小
for i in range(1, num_labels):
    if stats[i, cv2.CC_STAT_AREA] >= min_size:
        output[labels == i] = colors[i]
        # 画边界框和质心
        cv2.rectangle(output,
                      (stats[i, cv2.CC_STAT_LEFT], stats[i, cv2.CC_STAT_TOP]),
                      (stats[i, cv2.CC_STAT_LEFT] + stats[i, cv2.CC_STAT_WIDTH],
                       stats[i, cv2.CC_STAT_TOP] + stats[i, cv2.CC_STAT_HEIGHT]),
                      (0, 255, 0), 2)
        cv2.circle(output, (int(centroids[i][0]), int(centroids[i][1])), 4, (0, 0, 255), -1)

# 显示原图、二值化图像和连通域分析结果
print('num_labels = ', num_labels-1)
cv2.imshow('Original', img)
cv2.imshow('Binary', binary)
cv2.imshow('Connected Components', output)
cv2.waitKey(0)
cv2.destroyAllWindows()