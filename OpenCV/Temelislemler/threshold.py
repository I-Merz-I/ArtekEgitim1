import cv2
import numpy as np

img = cv2.imread("klon.jpg",0)

ret,th1= cv2.threshold(img,120,150,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow("Orjinal",img)
cv2.imshow("Threshold Binary",th1)
cv2.imshow("Adaptive Mean Threshold",th2)
cv2.imshow("Adaptive Gaussian Threshold",th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
