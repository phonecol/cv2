import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

img_bgr = cv2.imread('50ppm1.png')
img_rgb = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)

matrix = np.ones(img_rgb.shape, dtype = "uint8")* 50

img_rgb_brighter = cv2.add(img_rgb, matrix)

img_rgb_darker = cv2.subtract(img_rgb, matrix)

b,g,r = cv2.split(img_rgb)


a = plt.hist(b.ravel(),256,[0,256]);
aa = plt.hist(g.ravel(),256,[0,256]);
aaa = plt.hist(r.ravel(),256,[0,256]);

# bHist=plt.hist(b.ravel(),256,[0,256])
# gHist=plt.hist(g.ravel(),256,[0,256])
# rHist=plt.hist(r.ravel(),256,[0,256])

plt.figure(figsize = [18,5])
plt.subplot(231);plt.imshow(img_rgb_darker); plt.title("Darker");
plt.subplot(232);plt.imshow(img_rgb); plt.title("Original");
plt.subplot(233);plt.imshow(img_rgb_brighter); plt.title("Brighter");
# # plt.subplot(144);plt.imshow(bHist); plt.title("Histogram");
# plt.subplot(234); plt.hist(img_rgb_darker.ravel(),256,[0,256]);plt.title("Darker");
# plt.subplot(235);plt.hist(img_rgb.ravel(),256,[0,256]); plt.title("Original");
# plt.subplot(236);plt.hist(img_rgb_brighter.ravel(),256,[0,256]); plt.title("Brighter");

plt.subplot(234); plt.hist(b.ravel(),256,[0,256]);plt.title("Darker");
plt.subplot(235);plt.hist(g.ravel(),256,[0,256]); plt.title("Original");
plt.subplot(236);plt.hist(r.ravel(),256,[0,256]); plt.title("Brighter");




plt.show()

