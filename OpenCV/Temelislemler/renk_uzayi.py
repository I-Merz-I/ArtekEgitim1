import cv2
import numpy as np

img = cv2.imread("klon.jpg")

img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# cv2.imshow("Original Image", img)
# cv2.imshow("RGB Image", img_rgb)
# cv2.imshow("HSV Image", img_hsv)
# cv2.imshow("Gray Image", img_gray)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap = cv2.VideoCapture("1.mp4")

while True:
    ret,frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if ret == False:
        break
    cv2.imshow("Video Frame",frame)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

