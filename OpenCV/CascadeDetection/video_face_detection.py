import cv2

vid= cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(r"C:\Users\Muharrem\Downloads\haarcascade_frontalface_alt.xml")

while True:
    ret,frame = vid.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow("Face Detection", frame)
    key = cv2.waitKey(30) & 0xFF
    if key == 27:  # ESC to exit
        break

vid.release()
cv2.destroyAllWindows()