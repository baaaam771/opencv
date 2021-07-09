import cv2

source = cv2.imread('data/images/sample.jpg', 1)

print(source.shape)

cv2.imshow('original', source)

# 센터 좌표를 얻기 :넘파이의 형렬인 행과 열의 정보로 부터, 선터 좌표를 만들때 주의점
# 행렬을 좌표로 바꿀 때, 향은 좌표 y값이 되고 열은 좌표의 x 값이 된다

centerY = source.shape[0] / 2
centerX = source.shape[1] / 2

rotationAngle = 30
scaleFactor = 1

# 회전을 시킬수 있는 행렬을 우리한테 준다

rotationMatrix = cv2.getRotationMatrix2D(center=(centerX, centerY), angle=rotationAngle, scale=scaleFactor)

print(rotationMatrix)


# 행렬을 좌표로 바꿀 때, 향은 좌표 y값이 되고 열은 좌표의 x 값이 된다
result = cv2.warpAffine(source, rotationMatrix, (source.shape[1], source.shape[0]))

cv2.imshow('rotation img', result)


cv2.waitKey(0)
cv2.destroyAllWindows()