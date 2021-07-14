import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

for _ in range(10):
    _, frame = cap.read()
frame = cv2.resize(frame, (640, 480))
frame = cv2.flip(frame, 1)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray, (25, 25), 0)

background = gray

last_frame = gray

# cv2.imshow("Background", background)

while True :
    _, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    frame = cv2.flip(frame, 1)

    # processing
    # F : Foreground
    # B : Background

    # 지금까지는 아래처럼 동작하도록 했지만
    # F[i] = abs(Frame[i] - B)

    # 우리가 하고자 하는것은 아래처럼, 바로 전 프레임과, 현재 피레임의 차이를 얻어오는것
    # F[i] = abs(Frame[i-1] - Frame[i])

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (25, 25), 0)

    # foreground = gray - background

    # _, mask = cv2.threshold(foreground, 127, 255, cv2.THRESH_BINARY)

    abs_diff = cv2.absdiff(last_frame, gray)

    last_frame = gray

    _, ad_mask =cv2.threshold(abs_diff, 63, 255, cv2.THRESH_BINARY)

    dlilated_mask = cv2.dilate(ad_mask, None, iterations=2)

    # cv2.imshow("Foreground", foreground)

    # cv2.imshow("Mask", mask)
    cv2.imshow("Abs diff mask", ad_mask)
    cv2.imshow("Dilated mask", dlilated_mask)

    if cv2.waitKey(1) == ord('q'):
        break








# import cv2

# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# for _ in range(10):
#     _, frame = cap.read()
# frame = cv2.resize(frame, (640, 480))
# frame = cv2.flip(frame, 1)
# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# gray = cv2.GaussianBlur(gray, (25,25), 0)

# background = gray

# last_frame = gray

# # cv2.imshow("Background", background)

# while True :
#     _, frame = cap.read()
#     frame = cv2.resize(frame, (640, 480))
#     frame = cv2.flip(frame, 1)

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     gray = cv2.GaussianBlur(gray, (25, 25), 0)

    
#     abs_diff = cv2.absdiff(last_frame, gray)

#     last_frame = gray

#     _, ad_mask = cv2.threshold(abs_diff, 63, 255, cv2.THRESH_BINARY)

#     dilated_mask = cv2.dilate(ad_mask, None, iterations=2)
    
#     cv2.imshow("Abs diff mask", ad_mask)
#     cv2.imshow('Dilated mask', dilated_mask)

#     if cv2.waitKey(1) == ord('q'):
#         break
