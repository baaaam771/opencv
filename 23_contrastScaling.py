import cv2
import numpy as np

img  = cv2.imread('data/images/candle.jpg', 1)

scaleFactor = 3.5

# 1. 컬러스페이스 변경
ycbImage = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# 2.연산을 위해서 float로 변경
ycbImage = np.float32(ycbImage)

# 3.채널분리
Y, Cr, Cb = cv2.split(ycbImage)

# 4.연산
Y = Y * scaleFactor

# 5. clip 적용
Y = np.clip(Y, 0, 255)

# 6.합치기
ycbImage =cv2.merge( [Y, Cr, Cb] )

# 6-2 uin8로 변경
ycbImage = np.uint8(ycbImage)

# 7. 컬러스페이스 변경
ycbImage = cv2.cvtColor(ycbImage, cv2.COLOR_YCrCb2BGR)

# 8. 화면에 표시 => 하나의 윈도우에,  두 개의 이미지를 합쳐서 표시
# img, ycbImage 이 두개의 이미지를, 하나의 윈도우에, 2개가 옆으로 나타나도록
# np.hstack() 함수 : 여러개의 넘파이를 수평으로 붙여주는 함수
# np.vstack() 함수 : 여러개의 넘파이를 수직으로 붙여주는 함수

# combined = np.hstack( [img, ycbImage] )
combined = np.vstack( [img, ycbImage] )

cv2.imshow("combined", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()