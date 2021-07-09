import cv2
import numpy as np

# 캠으로부터 데이터 가져오기

cap = cv2.VideoCapture(0)

if cap.isOpened() == False :
    print('Unable to read camera feed')

else :
    
    # 프레임 정보 가져오기 : 화면 크기 (width, height)
    frame_width = int( cap.get(3) )
    frame_height = int( cap.get(4) )

    out = cv2.VideoWriter('data/videos/output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

    # 캠으로부터 사진을 계속 입력 받는다
    while True:
        ret, frame = cap.read()

        if ret == True:
            # 동영상으로 저장
            out.write(frame)
            # 화면에 표시
            cv2.imshow('frame', frame)
            
            # esc누르면 exit/ 캠 중간에 끄고 싶을 때
            if cv2.waitKey(25) & 0xFF ==27 :
                break

        else :
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()





