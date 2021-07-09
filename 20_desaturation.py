import cv2
import numpy as np

img = cv2.imread('data/images/capsicum.jpg', 1)

cv2.imshow('original', img)

saturationScale = 0.01

hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


# unit로 되어 있는 값을 float32로 바꿔준다 
hsvImage = np.float32(hsvImage)

# 각각의 h, s, v 채널을 분리한다. 즉 3차원 행렬을 2차원 행렬 3개로 분리한다.
H, S, V = cv2.split(hsvImage)

# 유용한함수 np.clip함수 이용
# 이 함수를 이용하면 0보다 작은 값은 0으로 바꾸고 255보다 크면 255로 자동으로 바꿔줄수 있다

S = S * saturationScale

S = np.clip(S, 0, 255)

# 채도 조절은 끝났다

# 이제 할일은, 각각 쪼개져 있는 행렬들을, 다시 원상복구 하나로 합치는 작업 필요
# 나눈 채널을 하나로 합치는 함수 cv2.merge
hsvImage = cv2.merge( [H, S, V] ) 


# 계산을 위해서 float32로 바꾼 데이터를 이제 다시 원상복구, uint8로 변경해준다
hsvImage = np.uint8(hsvImage)


# 우리눈으로 확인해볼 수 있도록 하기 위해서는, cv2.imshow()가 필요하며
# 이 함수는 컬러스페이스가 BGR로 되어 있어야, 우리눈에정확히 보여줄 수 있다
imgBgr = cv2.cvtColor(hsvImage, cv2.COLOR_HSV2BGR)

cv2.imshow('CVT BGR', imgBgr)





cv2.waitKey(0)
cv2.destroyAllWindows()