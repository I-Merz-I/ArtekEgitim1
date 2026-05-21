import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("Settings")
cv2.createTrackbar("Low H","Settings",0,179,nothing)
cv2.createTrackbar("Low S","Settings",0,255,nothing)
cv2.createTrackbar("Low V","Settings",0,255,nothing)
cv2.createTrackbar("High H","Settings",0,179,nothing)
cv2.createTrackbar("High S","Settings",0,255,nothing)
cv2.createTrackbar("High V","Settings",0,255,nothing)

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("Low H","Settings")
    ls = cv2.getTrackbarPos("Low S","Settings")
    lv = cv2.getTrackbarPos("Low V","Settings")
    hh = cv2.getTrackbarPos("High H","Settings")
    hs = cv2.getTrackbarPos("High S","Settings")
    hv = cv2.getTrackbarPos("High V","Settings")

    lower_color = np.array([lh,ls,lv])
    upper_color = np.array([hh,hs,hv])

    mask = cv2.inRange(hsv,lower_color,upper_color) # hsv renk uzayında belirlediğimiz renk aralığında bir maske oluşturuyoruz
    kernel = np.ones((5,5),np.uint8) # bu mask'teki gürültüyü azaltmak için bir kernel oluşturuyoruz
    mask = cv2.erode(mask,kernel,iterations=1) # mask'i erode ederek gürültüyü azaltıyoruz
    contours, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt) # konturun alanını hesaplıyoruz
        approx = cv2.approxPolyDP(cnt,0.02*cv2.arcLength(cnt,True),True) # konturun köşe sayısını bulmak için approxPolyDP fonksiyonunu kullanıyoruz
        approx.ravel()[0] # konturun ilk köşesinin x koordinatını alıyoruz
        approx.ravel()[1] # konturun ilk köşesinin y koordinatını alıyoruz
        if area > 400: # konturun alanı 400'den büyükse
            cv2.drawContours(frame,[approx],0,(0,255,0),5) # konturu yeşil renkte çiziyoruz
            if len(approx) == 3:
                cv2.putText(frame,"Triangle",(approx.ravel()[0],approx.ravel()[1]),font,0.5,(0,255,0),2) # konturun köşe sayısı 3 ise "Triangle" yazıyoruz
            elif len(approx) == 4:
                cv2.putText(frame,"Rectangle",(approx.ravel()[0],approx.ravel()[1]),font,0.5,(0,255,0),2) # konturun köşe sayısı 4 ise "Rectangle" yazıyoruz
            elif len(approx) == 5:
                cv2.putText(frame,"Pentagon",(approx.ravel()[0],approx.ravel()[1]),font,0.5,(0,255,0),2) # konturun köşe sayısı 5 ise "Pentagon" yazıyoruz
            elif len(approx) == 6:
                cv2.putText(frame,"Hexagon",(approx.ravel()[0],approx.ravel()[1]),font,0.5,(0,255,0),2) # konturun köşe sayısı 6 ise "Hexagon" yazıyoruz
            elif len(approx) == 10:
                cv2.putText(frame,"Star",(approx.ravel()[0],approx.ravel()[1]),font,0.5,(0,255,0),2) # konturun köşe sayısı 10 ise "Star" yazıyoruz 
            else:
                cv2.putText(frame,"Circle",(approx.ravel()[0],approx.ravel()[1]),font,0.5,(0,255,0),2) # konturun köşe sayısı 10'dan büyükse "Circle" yazıyoruz 
            
        

    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
