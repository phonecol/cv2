###Read an image from file (using cv::imread)
#Display an image in an OpenCV window (using cv::imshow)
#Write an image to a file (using cv::imwrite)

import cv2 as cv
import sys

img = cv.imread('50ppm1.png')

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite('starry_night.png', img)