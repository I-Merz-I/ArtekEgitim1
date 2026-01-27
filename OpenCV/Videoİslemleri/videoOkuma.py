import cv2

cap = cv2.VideoCapture(0)  # Bilgisayarın varsayılan kamerasını aç


while True:
    ret , frame = cap.read()  # Kameradan bir kare oku
    frame = cv2.flip(frame,1)   # Kareyi yatay olarak çevir
    cv2.imshow("webcam",frame) # Kareyi ekranda göster
    if cv2.waitKey(30) & 0xFF == ord('q'):  # 'q' tuşuna basılırsa çık
        break

cap.release()  # Kamerayı serbest bırak
cv2.destroyAllWindows()  # Tüm OpenCV pencerelerini kapat