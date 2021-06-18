##Learn to draw different geometric shapes with OpenCV
#You will learn these functions : cv.line(), cv.circle() , cv.rectangle(), cv.ellipse(), cv.putText() etc.

import numpy as np
import cv2 as cv

img = np.zeros((512,512,3), np.uint8)

cv.line(img, (0,0),(512,512),(255,0,0),1)
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv.circle(img,(447,63), 63, (0,0,255), 2)
cv.ellipse(img,(256,256),(100,50),0,0,180,255,1)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

cv.imshow('drawing',img)
cv.waitKey(0)