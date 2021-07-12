import cv2
import numpy as np

img = cv2.imread('data/images/candle.jpg', 1)

ycbImage = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

Y, Cr, Cb = cv2.split(ycbImage)

# 히스토그래 균일화하는 함수 : cv2.equalizeHist()
# 이 함수 자체가 연산을 해서 주기 때문에, 이 함수 내주에서 알아서
# float으로 바꾸고, 알아서 0~255 사이의 값으로 가시 셋팅해서
# uint8로 바꿔서 돌려준다
# 
# 따라서 저희는 함수만 호출하면 된다 
Y = cv2.equalizeHist(Y)

print(Y)
print(Y.dtype)

ycbImage = cv2.merge( [Y, Cr, Cb] )

ycbImage = cv2.cvtColor(ycbImage, cv2.COLOR_YCrCb2BGR)

combined = np.hstack([img, ycbImage])

cv2.imshow("combined", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()