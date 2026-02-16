import cv2 
import numpy as np

cap = cv2.VideoCapture("dog.mp4")

while True:
    _,frame = cap.read()
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    sensitivity = 15
    lower = np.array([0,0,255-sensitivity])
    upper = np.array([255,sensitivity,255])

    mask = cv2.inRange(hsv,lower,upper)
    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)
    cv2.imshow("result",res)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
