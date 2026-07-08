import cv2
import numpy as np

vid = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(r"C:\Users\Muharrem\Downloads\haarcascade_frontalface_alt.xml")
eye_cascade = cv2.CascadeClassifier(r"C:\Users\Muharrem\Downloads\haarcascade_eye.xml")

while True:
    ret, frame = vid.read()
    if not ret:
        break

    frame = cv2.resize(frame, (480, 360))
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        roi_frame = frame[y:y + h, x:x + w]
        roi_gray = gray[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray,1.3,6)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_frame, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

    cv2.imshow("video", frame)
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()

