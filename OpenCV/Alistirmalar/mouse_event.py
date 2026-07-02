import cv2

cap = cv2.VideoCapture(r"C:\Users\Muharrem\Documents\GitHub\ArtekEgitim1\OpenCV\Alistirmalar\15556727_540_960_60fps.mp4")
circles = []
def mouse(event,x,y,flags,params): # mouse eventlerini yakalamak için bir fonksiyon tanımlıyoruz.
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Mouse clicked at: ({x}, {y})")
        circles.append((x, y))

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse) # setmousecallback fonksiyonu ile mouse eventlerini yakalıyoruz.

while True:
    _,frame = cap.read()
    for center in circles:
        cv2.circle(frame,center,20,(0,255,0),-1) # mouse ile tıklanan noktalara daire çiziyoruz.

    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC key
        break
    elif key == ord('c'):  # 'c' key
        circles.clear()  # Clear the list of circles

cap.release()
cv2.destroyAllWindows()