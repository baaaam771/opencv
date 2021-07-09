from typing import TYPE_CHECKING
import cv2
import numpy as np

image = cv2.imread('data/images/mark.jpg')

cv2.imshow('img', image)

# 선그리기

imageLine = image.copy()

cv2.line(imageLine, (322, 179), (400, 183), (0, 0, 255), thickness=2, lineType=cv2.LINE_AA)
# (BGR)
cv2.imshow('image line', imageLine)



# 원 그리기

imageCircle = image.copy()

cv2.circle(imageCircle, (350, 200), 150, (255, 0, 0), thickness=3, lineType=cv2.LINE_AA)

cv2.imshow('image circle', imageCircle)


# 타원 그리기

imageEllipse = image.copy()

cv2.ellipse(imageEllipse, (360, 200), (100, 170), 45, 0, 360, (0, 255, 0), thickness=2 )

cv2.ellipse(imageEllipse, (360, 200), (100, 170), 135, 0, 360, (0, 0, 255), thickness=2)

cv2.imshow('ellipse', imageEllipse)



# 사각형 그리기

imageRectangle = image.copy()

cv2.rectangle(imageRectangle, (208, 55), (450, 355), (255, 0, 0), thickness=3)

cv2.imshow('rectangle', imageRectangle)



# 글자넣기

imageText = image.copy()
cv2.putText(imageText, "Mark Zuckerberg", (205, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), thickness=2)

cv2.imshow('text', imageText)


# 시습 : 마크 주커버그 얼굴에 사각형 그리고, 그 위에 Mark Zuckerberg 라고 글자를 넣으시오.
ImageRep = image.copy()
cv2.rectangle(ImageRep, (208, 55), (450, 355), (255, 0, 0), thickness=3)
cv2.putText(ImageRep, "Mark Zuckerberg", (205, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), thickness=2)


cv2.imshow('Rep', ImageRep)

cv2.waitKey(0)
cv2.destroyAllWindows()