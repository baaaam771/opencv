import cv2
import numpy as np


# 첫번째 사진의 3점의 좌표
input_triangle = np.array([50, 50, 100, 100, 200, 200], dtype='float32')

# 삼각형 3점의 좌표로 변환
input_triangle = input_triangle.reshape(3, 2)

print(input_triangle)


# 변환된 사진의 세점의 좌표
output_triangle = np.float32([70, 76, 142, 101, 272, 136])

output_triangle = output_triangle.reshape(3, 2)

print(output_triangle)



warpMat = cv2.getAffineTransform(input_triangle, output_triangle)

print(warpMat)