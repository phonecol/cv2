import numpy as np
import cv2
from matplotlib import pyplot as plt

paperSensors = []
for i in range(0,12):
   paperSensor = cv2.imread("50ppm"+str(i)+".PNG")
   paperSensors.append(paperSensor)

for j in range(0,12):

    img = paperSensors[j+1]
    b,g,r = cv2.split(img)

    cv2.imshow("img",img)
    cv2.imshow("b",r)
    cv2.imshow("g",g)
    cv2.imshow("r",r)

    plt.hist(b.ravel(),256,[0,256])
    plt.hist(g.ravel(),256,[0,256])
    plt.hist(r.ravel(),256,[0,256])
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()