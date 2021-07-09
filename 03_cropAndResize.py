import cv2


# 1은 칼라이미지, 0은 그레이스케일, -1은 알파채널 포함한 이미지
source = cv2.imread('data/images/sample.jpg', 1)

# 실수로 사용
scaleX = 0.6 #x축은 60%
scaleY = 0.6

scaleDown = cv2.resize(source, None, fx=scaleX, fy=scaleY, interpolation=cv2.INTER_LINEAR)

cv2.imshow('Original', source)
cv2.imshow('Scaled Down', scaleDown)

scaleX=2.3
scaleY=1.6

scaleUp = cv2.resize(source, None, fx=scaleX, fy=scaleY, interpolation=cv2.INTER_LINEAR) 

# cv2.imshow('Scale Up', scaleUp)

# crop : 내가 원하는 부분만 이미지를 자르는 것
# 넘파이를 슬라이싱 하는 것과 같다

crop_img = source[ 10 : 200 , 150 : 450 ]
cv2.imshow("Crop Img", crop_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

