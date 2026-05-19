import cv2
import numpy as np

img = cv2.imread("C:/Users/muhar/OneDrive/Belgeler/GitHub/ArtekEgitim1/OpenCV/ContourIslemleri/map.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray,(3,3))
ret,thresh = cv2.threshold(blur,40,255,cv2.THRESH_BINARY)

countours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

hull = []

for i in range(len(countours)):
    hull.append(cv2.convexHull(countours[i],False))

bg = np.zeros((thresh.shape[0],thresh.shape[1],3),dtype=np.uint8)

for i in range(len(countours)):
    cv2.drawContours(bg,countours,i,(255,0,0),3,8,hierarchy)
    cv2.drawContours(bg,hull,i,(0,255,0),3,8,hierarchy)

cv2.imshow("Contours",bg)
cv2.waitKey(0)
cv2.destroyAllWindows()