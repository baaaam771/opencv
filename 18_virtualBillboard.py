import cv2
import numpy as np

from utils import get_four_points

# 이번에는 똑바른 이미지를 찌그러뜨린 이미지로 변환하려고 합니다
img_src = cv2.imread('data/images/first-image.jpg', 1)

cv2.imshow("img_src", img_src)


img_dst = cv2.imread('data/images/times-square.jpg', 1)

# cv2.imshow("Img dst", img_dst)

print(img_src.shape)
# (477, 600, 3)

# 똑바른 이미지릐 4개의 점 좌표를 가져오고

points_src = np.array( [0, 0,   img_src.shape[0], 0,   img_src.shape[1], img_src.shape[0],   0, img_src.shape[0]] )

points_src = points_src.reshape(4,2)

print(points_src)

# 찌그러진 이미지의 4개 점은, 바로 못가져오니까, 마우스로 찍어서 점의 좌표를 받아온다

points_dst = get_four_points(img_dst)

print(points_dst)


H, status = cv2.findHomography(points_src, points_dst)

print(H)

img_temp = cv2.warpPerspective(img_src, H, (img_dst.shape[1], img_dst.shape[0]))


cv2.imshow("Img temp", img_temp)




# 타임스 스퀘어의 전광판 안쪽 영역을 0으로 만들고, 두개의 이미지를 합져 버리면, 하나의 이미지로 완성된다 
cv2.fillConvexPoly(img_dst, points_dst.astype(int), 0)

cv2.imshow("img_dst", img_dst)


img_result = img_dst + img_temp

cv2.imshow("result", img_result)


cv2.waitKey(0)
cv2.destroyAllWindows()
