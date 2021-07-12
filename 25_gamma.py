import cv2
import numpy as np

img = cv2.imread('data/images/candle.jpg', 1)

cv2.imshow("original", img)

gamma = 1.5


# 이미지는 0부터 255까지이므로, 이 이미지 범위에 해당하는 모든 숫자를 가져온다.

fullRange = np.arange(0, 255+1)

print(fullRange)


# 감마보정을 통해서, 원래의 0~255까지의 숫자를  => 보정한 숫자로 변경한다

LookupTable = 255 * np.power ((fullRange / 255.0) , gamma )


# 감마보정을 통해서 나온 연산 결과는, Float이므로, uint8로 다시 변경해야한다.

LookupTable = np.uint8(LookupTable)

# 즉, 0~255를 감마보정을 통해 대칭된 숫자를 얻어온다 그것이 LookupTable
print(LookupTable)


# 이를 cv2.LUT함수를 통해서
# 원본이미지를 내가 원하는 룩업테이블의 값으로 매칭하여, 변경해준 이미지로 얻어온다
# LUT = lookupTable

output = cv2.LUT(img, LookupTable)

combined = np.hstack([img, output])

cv2.imshow("combined", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()