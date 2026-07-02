import cv2 
import numpy as np

''' Manuel olarak ilk frame'i alıp, onu referans frame olarak kullanıyoruz.
    Daha sonra her frame'i referans frame ile karşılaştırıp, farkını alıyoruz.

cap = cv2.VideoCapture(0)
_,first_frame = cap.read()
first_gray = cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray,(5,5),0)


while True:

    _,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(5,5),0)

    diff = cv2.absdiff(first_gray, gray)
    _,diff = cv2.threshold(diff,65,255,cv2.THRESH_BINARY)

    cv2.imshow("First Frame",first_frame)
    cv2.imshow("Current Frame",frame)
    cv2.imshow("Difference",diff)
    key = cv2.waitKey(30)
    if key == 27:  # ESC key
        break
'''
# otomatik olarak referans frame'i alıp, her frame'i referans frame ile karşılaştırıp, farkını alıyoruz.
cap = cv2.VideoCapture(r"C:\Users\Muharrem\Documents\GitHub\ArtekEgitim1\OpenCV\Alistirmalar\15556727_540_960_60fps.mp4")
subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=120, detectShadows=True)

while True:
    _,frame  = cap.read()
    mask = subtractor.apply(frame)

    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)

    if cv2.waitKey(30) & 0xFF == 27:  # ESC key
        break
    
