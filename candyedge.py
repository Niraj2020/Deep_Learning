import cv2
import numpy as np
from datetime import timedelta
import matplotlib

img=cv2.imread("Data\\building.jpg")
img=cv2.resize(img, (600, 700))
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def nothing(x):
    pass

cv2.namedWindow("Candy")
cv2.createTrachbar("Threshold", "Candy", 0, 255, nothing)

while True:
    a=cv2.Candy(img_gray, a, 255)
    cv2.imshow("Candy", res)
    k=cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindowa()    