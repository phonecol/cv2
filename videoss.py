#Learn to read video, display video, and save video.
#Learn to capture video from a camera and display it.
#You will learn these functions : cv.VideoCapture(), cv.VideoWriter()

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print('Cannot open camera')
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("cant receive frame (stream end?)")
        break

    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()