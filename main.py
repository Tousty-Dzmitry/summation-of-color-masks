import numpy as np
import cv2

# с видио камеры
#capImg = cv2.VideoCapture(0)

# с видео ролик
capImg = cv2.VideoCapture('colored objects.mp4')

while(capImg.isOpened()):

    ret, frame = capImg.read()

    if frame is None:
        break

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    crop_frame = frame[60:270, 30:750]
    crop_frame_hsv = frame_hsv[60:270, 30:750]


    low_Blue = np.array([105, 150, 0], dtype='uint8')
    high_Blue = np.array([135, 255, 210], dtype='uint8')

    low_Yel = np.array([10, 150, 100], dtype='uint8')
    high_Yel = np.array([50, 255, 255], dtype='uint8')

    low_Red_O = np.array([0, 85,110], dtype='uint8')
    high_Red_O = np.array([5, 165, 155], dtype='uint8')

    low_Red_V = np.array([165, 55, 40], dtype='uint8')
    high_Red_V = np.array([180, 105, 120], dtype='uint8')

    blue_mask = cv2.inRange(crop_frame_hsv, low_Blue, high_Blue)

    yel_mask = cv2.inRange(crop_frame_hsv, low_Yel, high_Yel)

    red1_mask = cv2.inRange(crop_frame_hsv, low_Red_O, high_Red_O)

    red2_mask = cv2.inRange(crop_frame_hsv, low_Red_V, high_Red_V)

    full_mask = red1_mask + red2_mask + blue_mask + yel_mask


    cv2.imshow('video_mask', full_mask)

    cv2.imshow('video_frame', crop_frame)

    key_press = cv2.waitKey(30)
    if key_press == ord('q'):
        break

capImg.release()
cv2.destroyAllWindows()

