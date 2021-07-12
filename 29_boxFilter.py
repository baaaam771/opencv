import cv2
import numpy as np

img = cv2.imread('data/images/gaussian-noise.png', 1)

# 3X3 커널을 컨볼루션해서 얻은 피처맵 이미지 dst1
dst1 = cv2.blur(img, (3, 3))

#7X7 커널도 사용
dst2 = cv2.blur(img, (7, 7))

combined = np.hstack([img, dst1, dst2])

cv2.imshow("combined", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()