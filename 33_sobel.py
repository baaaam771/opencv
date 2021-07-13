import cv2
import numpy as np

img = cv2.imread('data/images/truth.png')

cv2.imshow('original', img)

sobelX = cv2.Sobel(img, cv2.CV_32F, 1, 0)

sobelY = cv2.Sobel(img, cv2.CV_32F, 0, 1)


cv2.imshow('sobelX', sobelX)
cv2.imshow('sobelY', sobelY)



cv2.waitKey(0)
cv2.destroyAllWindows()

