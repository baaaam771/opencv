import cv2
import numpy as np

cap = cv2.VideoCapture('data/videos/chaplin.mp4')

if cap.isOpened() == False:
    print('Error opening video stream or file')

else:

    # 반복분이 필요한 이유?
    # 비디오는 여러장의 사진으로 구성되어 있으므로, 
    # 반복문을 통해서, 여러 사진을 한장씩 처리해야한다.
    while cap.isOpened():

        # 사진을 1장씩 가져온다.
        ret, frame = cap.read()

        # ret에는 사진을 제대로 가져왔는지의 정보가 True, False로 들어있다
        # 따라서 ret가 트루이면 우리는 화면에 사진-넘파이 어레이(frame)을 표시하면 된다.
        if ret == True:

            cv2.imshow("Frame", frame)

            #키보드에서 esc를 누르면 exit하하는 코드작성
            # 비디오 실행 중간에, 끄고 싶을떄 사용한다
            if cv2.waitKey(25) & 0xFF ==27 :
                break

        else:

            # 동영상 재생이 끝난 경우, 또는 동영상 사진이 이상이 있는 경우
            break

    cap.release()

    cv2.destroyAllWindows()
