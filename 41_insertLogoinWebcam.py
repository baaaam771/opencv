# 실습 : 웹캠에 로고 넣기 실습

# 1. logo.png 파일을 읽어오기

# 2. 위파일을 (100, 100)으로 리사이징 하기

# 3. 그레이스케일로 바꾸기
# 
# 4. 쓰레솔드 이용해서 로고를 마스킹하기
# 
# 5. 웹캠을 640, 480로 설정해서 켜고 
# 
# 6. 웹캠 이미지에서, 오른쪽 아래에 로고를 표시할 Region Of Interest를 셋팅합니다
# 
# 7. 로고와 웹캠 이미지를 합칩니다. 

import cv2
import numpy as np

logo = cv2.imread('data/images/logo.png')

logo = cv2.resize(logo, (100, 100))

cv2.imshow('logo', logo)

gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)

_, mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

# cv2.imshow('gray', gray)
cv2.imshow('mask', mask)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# while True :
#     # ret, frame = cap.read()
#     _, frame = cap.read()

#     frame = cv2.resize(frame, (640, 480))
#     frame = cv2.flip(frame, 1)

#     # roi = frame[-100-10 : -10+1, -100-10 : -10+1]
#     roi = frame[370 : 470, 530 : 630]
#     roi[np.where(mask)] = 0

#     roi = roi + logo

#     cv2.imshow('Webcam', frame)

#     if cv2.waitKey(1) == ord('q'):
#         break

while True:
    _, frame = cap.read()
    # This is the processing
    frame = cv2.resize(frame, (640, 480))
    frame = cv2.flip(frame, 1)

    roi = frame[-100-10:-10, -100-10:-10]
    roi[np.where(mask)] = 0
    roi += logo

    # Here we show the image in a window
    cv2.imshow("Webcam", frame)

    # Check if q was pressed
    if cv2.waitKey(1) == ord('q'):
        break




# cv2.waitKey(0)
# cv2.destroyAllWindows()