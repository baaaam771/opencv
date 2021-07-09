import cv2

imageName = "data/images/truth.png"

image = cv2.imread(imageName, cv2.IMREAD_COLOR)

cv2.imshow("original", image)

# 이미지 경계 축소(침식)

dilationSize = 3

element = cv2.getStructuringElement(cv2.MORPH_RECT, (2*dilationSize +1, 2*dilationSize+1))

imageEroded = cv2.erode(image, element)

cv2.imshow("Erodsion", imageEroded)

cv2.waitKey(0)
cv2.destroyAllWindows()