import cv2
import numpy as np

original = cv2.imread('data/images/girl.jpg')

# cv2.imshow("original", original)

img = original.copy()

# 행렬에 들어 있는 원래의 기준값 6개 셋팅
originalValue = np.array([0, 50, 100, 150, 200, 255])

# 위의 기준값에 대칭되는 6개의 값 셋팅
# 이 값은, 기준값보다 높은 값들이다.
# 즉 기준값이 있으면 그 값을 각각 아래의 올려서 매칭
rCurve = np.array([0 ,80, 150, 190, 220, 255])

# 위 기준값에 매칭 되는 6개의 값인데,  각 기준값보다 작은 값으로 매칭됨
bCurve = np.array([0, 20, 40, 75, 150, 255])

#Lookup Table만들기
# 현재, 6개의 기준점만 가지고 있다
# 그렇지만 우리는, 256개의 모든 점으로 만들어줘야한다.
# 그래야 0~255까지의 값들을 해당 룩업테이블로 매칭시켜 줄 수 있기 때문에 6개의 기준점을 가지고,
# 총 256개의 매칭 점을 도출해야함

fullrange = np.arange(0, 255+1)

# 특정 갯수의 점들로, 점들을 늘리는 방법
rLUT = np.interp(fullrange, originalValue, rCurve)

# print(fullrange)
# print(rLUT)


bLUT = np.interp(fullrange, originalValue, bCurve)


# 원래의 원본 이미지에서, 우리는 R채널만 가져와서, rLUT를 적용하면 되고


# B, G, R = cv2.split(img)
R = img[ : , : , 2 ]

R = cv2.LUT(R, rLUT)

img[ : , : , 2] = R

# B채널만 가져와서 bLUT를 적용하면 된다.
B = img[ : , : , 0 ]

B = cv2.LUT(B, bLUT)

img[ : , : , 0] = B

combined = np.hstack([original, img])

cv2.imshow("combined", combined)


cv2.waitKey(0)
cv2.destroyAllWindows()