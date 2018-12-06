"""
第三章习题3.1色彩平衡
将每个色彩乘以一个指定的不同常量来改变一副图像的色彩平衡

注意：
png图片读取之后是以0~255间整数存储
如果乘以常数，可能导致出现小数值
这时imshow()会认为是一副以0~1内浮点数存储的图像
为了一致，将图片手动从0~255转换到0~1
"""
import cv2
import numpy as np


def nothing(x):
    pass


def gamma_transformation(img, gamma):
    return np.power(img,  gamma)


image = cv2.imread("1.png") / 255  # 将0~255整数储存转换为0~1浮点数储存

cv2.namedWindow("image")
cv2.namedWindow("origin")

# 调色栏
cv2.createTrackbar('R', 'image', 100, 500, nothing)
cv2.createTrackbar('G', 'image', 100, 500, nothing)
cv2.createTrackbar('B', 'image', 100, 500, nothing)

# 是否采用gamma变换
cv2.createTrackbar('do_gamma', 'image', 0, 1, nothing)

# gamma值
cv2.createTrackbar('gamma_value', 'image', 0, 30, nothing)

# 先后采用gamma变换
cv2.createTrackbar('gamma_before', 'image', 0, 1, nothing)

# 当前显示的图片
cur = image.copy()

while True:
    cv2.imshow("image", cur)
    cv2.imshow("origin", image)

    # 因为Trackbar不支持小数，自行转化为小数，原区间为0~500，除以100，转换为0~5内小数
    c_R = cv2.getTrackbarPos('R', "image") / 100
    c_G = cv2.getTrackbarPos('G', "image") / 100
    c_B = cv2.getTrackbarPos('B', "image") / 100

    gamma_value = cv2.getTrackbarPos('gamma_value', 'image')/10
    gamma_before = cv2.getTrackbarPos('gamma_before', 'image')
    do_gamma = cv2.getTrackbarPos('do_gamma', 'image')

    if do_gamma:
        if gamma_before:
            cur = gamma_transformation(image, gamma_value)
            cur[:, :, 0] = cur[:, :, 0] * c_B
            cur[:, :, 1] = cur[:, :, 1] * c_G
            cur[:, :, 2] = cur[:, :, 2] * c_R
        else:
            cur[:, :, 0] = image[:, :, 0] * c_B
            cur[:, :, 1] = image[:, :, 1] * c_G
            cur[:, :, 2] = image[:, :, 2] * c_R
            cur = gamma_transformation(cur, gamma_value)
    else:
        cur[:, :, 0] = image[:, :, 0] * c_B
        cur[:, :, 1] = image[:, :, 1] * c_G
        cur[:, :, 2] = image[:, :, 2] * c_R

    k = cv2.waitKey(1)
    if k == ord('q'):  # 按q退出
        break
