import cv2

# src = cv2.imread('data/images/threshold.png', cv2.IMREAD_GRAYSCALE)

# 0은 그레이스케일을 의미합니다
src = cv2.imread('data/images/threshold.png', 0)

cv2.imshow("Original", src)

# 이 값이 기준값이 되는 것
thresh = 100

# 이 값이 , 위의 기준값보다 큰 것들을 전부 이값으로 바꾸기 위해 사용
maxValue = 255

# 두번쨰 리턴 값인, dst가 쓰레숄드 적용된 이미지(넘파이 어레이)이다. 
th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY)

# dst를 화면에 표시한다
cv2.imshow("Thresholded Image", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()