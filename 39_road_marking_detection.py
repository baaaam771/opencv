import cv2
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

image_color = cv2.imread('data2/image.jpg')
# cv2.imshow('ori', image_color)

# 우리가 필요한 건, 그레이 스케일 이미지
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', image_gray)

image_copy = image_gray.copy()

print(image_copy.shape)

# 값이 195 미만인 것들은, 전부 0으로 셋팅한다. 
print(image_copy[ : , : ] <195)

image_copy[ image_copy[ : , : ] <195 ] = 0

# 흰색 차선 확인
# cv2.imshow("copy", image_copy)

image = cv2.imread('data2/test_image.jpg')
# cv2.imshow("img", image)

print('Height = ', image.shape[0], 'pixcels')
print('Width = ', image.shape[1], 'pixcels')

gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.imshow('gray', gray_img)

hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# cv2.imshow('hsv', hsv_img)


# Hue 채널만 가져와서, 화면에 보여준다
H, S, V = cv2.split(hsv_img)

H = hsv_img[ : , : , 0]

# cv2.imshow("Hue", H)

image = cv2.imread('data2/test_image2.jpg')
cv2.imshow('image', image)

M_rotation = cv2.getRotationMatrix2D( (image.shape[1] / 2, image.shape[0] /2) , 90, 0.5 )

rotated_img = cv2.warpAffine(image, M_rotation, (image.shape[1], image.shape[0]))

# cv2.imshow('rotated', rotated_img)



image = cv2.imread('data2/test_image3.jpg')
# cv2.imshow('image', image)

T_matrix = np.array([1, 0, 120, 0, 1, -150], dtype='float32')
T_matrix = T_matrix.reshape(2, 3)

print((T_matrix))

translation_image = cv2.warpAffine(image, T_matrix, (image.shape[1], image.shape[0]))
# cv2.imshow('tran', translation_image)


resized_image = cv2.resize(image, None, fx=0.5, fy=1.2, interpolation=cv2.INTER_LINEAR)
cv2.imshow('resize', resized_image)



cv2.waitKey(0)
cv2.destroyAllWindows()