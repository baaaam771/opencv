import cv2
import numpy as np

highThreshold = 100
lowThreshold = 50

# 화면 창에 적용할 변수
maxThreshold = 1000

apertureSizes = [3, 5, 7]

# 화면 창에 적용할 변수
maxapertureIndex = 2
apertureIndex = 0

# 화면 창에 적용할 변수
blurAmount = 0
maxBlurAmount = 20

# 트랙바 용 함수
# 케니 엣지 적용하는 함수 작성
def applyCanny():
    if blurAmount > 0:
        blurredSrc = cv2.GaussianBlur(src, (2*blurAmount+1, 2*blurAmount+1), 0)
    else:
        blurredSrc = src.copy()
    
    apertureSize = apertureSizes[apertureIndex]

    edges = cv2.Canny(blurredSrc, lowThreshold, highThreshold, apertureSize=apertureSize)

    cv2.imshow("Edges", edges)

# low therhold 적용하는 함수 : 트랙바에서 사용됨
def updateLowThreshold(*args):
    global lowThreshold
    lowThreshold = args[0]
    applyCanny()

# high therhold 적용하는 함수 : 트랙바에서 사용됨
def updateHighThreshold(*args):
    global highThreshold
    highThreshold = args[0]
    applyCanny()

# 블러 적용하는 함수
def updateBlurAmount(*args):
    global blurAmount
    blurAmount = args[0]
    applyCanny()

# aperture 적용하는 함수
def updateApertureIndex(*args):
    global apertureIndex
    apertureIndex = args[0]
    applyCanny()


src = cv2.imread('data/images/sample.jpg', 0)

edges = src.copy()

cv2.imshow('Edges', edges)
cv2.namedWindow('Edges', cv2.WINDOW_AUTOSIZE)

# low thershold에 대한 마우스 컨트롤러흫 트랙바에 붙인다
cv2.createTrackbar('Low Threshold', 'Edges', lowThreshold, maxThreshold, updateLowThreshold)
# high thershold에 대한 마우스 컨트롤러흫 트랙바에 붙인다
cv2.createTrackbar('High Threshold', 'Edges', highThreshold, maxThreshold, updateHighThreshold)
# aperture를 트랙바에 붙인다
cv2.createTrackbar('Aperture Size', 'Edges', apertureIndex, maxapertureIndex, updateApertureIndex)
# blur 컨트롤러를 트랙바에 붙인다
cv2.createTrackbar('Blur', 'Edges', blurAmount, maxBlurAmount, updateBlurAmount)


cv2.waitKey(0)
cv2.destroyAllWindows()