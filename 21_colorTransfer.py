from typing import no_type_check
import cv2
import numpy as np

src = cv2.imread('data/images/image1.jpg')
dst = cv2.imread('data/images/image2.jpg')

cv2.imshow('src', src)
cv2.imshow('dst', dst)

# 위 두 이미지의 컬러를 조합하여, 결과로 만들 이미지 생성
output = dst.copy()


srcLab = cv2.cvtColor(src, cv2.COLOR_BGR2LAB)
dstLab = cv2.cvtColor(dst, cv2.COLOR_BGR2LAB)
outputLab = cv2.cvtColor(output, cv2.COLOR_BGR2LAB)

# 연산을 위해서 float32로 변환

srcLab = srcLab.astype('float32') # np.float32(srcLab)
dstLab = dstLab.astype('float32') # np.float32(dstLab)
outputLab = outputLab.astype('float32')

print(srcLab)


cv2.waitKey(0)
cv2.destroyAllWindows()