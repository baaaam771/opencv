import cv2
import numpy as np

img_src = cv2.imread('data/images/book2.jpg')

# 첫번째 이미지 점 4개
point_src = np.array([141, 131, 480, 159, 493, 630, 64, 601], dtype='float')
point_src = point_src.reshape(4, 2)

print(point_src)


img_dst = cv2.imread('data/images/book1.jpg')

# 두번째 이미지 점 4개
point_dst = np.array([318, 256, 534, 372, 316, 670, 73, 473], dtype='float')
point_dst = point_dst.reshape(4,2)

print(point_dst)


# H : 호모 그래피 변황에 사용된 3X3행렬을 찾을 수 있다.

H, status = cv2.findHomography(point_src, point_dst)

print(H)

img_output = cv2.warpPerspective(img_src, H, (img_dst.shape[1], img_dst.shape[0]))

cv2.imshow('SRC', img_src)

cv2.imshow('DST', img_dst)

cv2.imshow('Warp', img_output)


cv2.waitKey()
cv2.destroyAllWindows()

