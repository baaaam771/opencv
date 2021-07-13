import cv2
import numpy as np

# 1. 이미지 가져오기
image = cv2.imread('data3/test_image.jpg', 1)

cv2.imshow('ori', image)

# 2.그레이 스케일로 변경
lanelines_image = image.copy()

gray_conversion = cv2.cvtColor(lanelines_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray_conversion)

# 3.smoothing
blur_conversion = cv2.GaussianBlur(gray_conversion, (5, 5), 0)

cv2.imshow('smooth', blur_conversion)

# 4. Canny Edge Detection
canny_conversion = cv2.Canny(blur_conversion, 50, 155)

cv2.imshow('canny', canny_conversion)

# 5. Masking ROI (Region Of Interest)

def reg_of_interest(image):
    image_height = image.shape[0]
    polygons = np.array([[(200, image_height), (1100, image_height), (550, 250)]])




cv2.waitKey(0)
cv2.destroyAllWindows()