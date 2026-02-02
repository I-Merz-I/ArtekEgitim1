import cv2
import numpy as np

cap=cv2.VideoCapture(0) 

def nothing(x):
    pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",400,300)

cv2.createTrackbar("L-H","Trackbars",0,179,nothing)
cv2.createTrackbar("L-S","Trackbars",0,255,nothing)
cv2.createTrackbar("L-V","Trackbars",0,255,nothing)

cv2.createTrackbar("U-H","Trackbars",179,179,nothing)
cv2.createTrackbar("U-S","Trackbars",255,255,nothing)
cv2.createTrackbar("U-V","Trackbars",255,255,nothing)

cv2.setTrackbarPos("U-H","Trackbars",179)
cv2.setTrackbarPos("U-S","Trackbars",255)
cv2.setTrackbarPos("U-V","Trackbars",255)   

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)

    frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L-H","Trackbars")
    l_s = cv2.getTrackbarPos("L-S","Trackbars")
    l_v = cv2.getTrackbarPos("L-V","Trackbars")
    u_h = cv2.getTrackbarPos("U-H","Trackbars")
    u_s = cv2.getTrackbarPos("U-S","Trackbars")
    u_v = cv2.getTrackbarPos("U-V","Trackbars")

    lower_colur = np.array ([l_h,l_s,l_v])
    upper_colur = np.array ([u_h,u_s,u_v])

    mask = cv2.inRange(frame_hsv,lower_colur,upper_colur)
    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()