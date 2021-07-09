import cv2
import numpy as np

def mouse_handler(event, x, y, flags, data):

    if event == cv2.EVENT_LBUTTONDOWN : 
        cv2.circle( data['image'], (x, y), 3, (0, 0, 255), 5, cv2.LINE_AA )

        cv2.imshow("Image", data['image'])

        if len(data['points']) < 4 :
            data['points'].append([x, y])


def get_four_points(image) :
    data = {}
    data['image'] = image.copy()
    data['points'] = []

    cv2.imshow("Image", image)
    cv2.setMouseCallback("Image", mouse_handler, data)

    cv2.waitKey(0)

    # 유저가 마우슬 점을 다 찍고 다른 키를 누르면, 점의 좌표들을 float로 바꿔줘야 한다.
    points =np.array( data['points'], dtype='float' ) 

    return points