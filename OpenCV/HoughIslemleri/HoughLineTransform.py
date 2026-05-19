import cv2 
import numpy as np

img = cv2.imread("C:/Users/muhar/OneDrive/Belgeler/GitHub/ArtekEgitim1/OpenCV/HoughIslemleri/houghline.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(gray,75,150)

lines = cv2.HoughLinesP(edge, 1, np.pi/180, threshold=50, minLineLength=40, maxLineGap=30)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2) 


cv2.imshow("gray",gray)
cv2.imshow("edeg",edge)
cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows
