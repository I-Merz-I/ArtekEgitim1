import cv2  
import numpy as np

img = cv2.imread("C:/Users/muhar/OneDrive/Belgeler/GitHub/ArtekEgitim1/OpenCV/HoughIslemleri/circle.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.medianBlur(gray, 5)

circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=50, param2=30, minRadius=0, maxRadius=0)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)

cv2.imshow("Detected Circles", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
