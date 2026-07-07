import cv2 

vid = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(r"C:\Users\Muharrem\Downloads\haarcascade_frontalface_alt.xml")
eye_cascade = cv2.CascadeClassifier(r"C:\Users\Muharrem\Downloads\haarcascade_eye.xml")

while 1: 
    ret,frame = vid.read()
    frame = cv2.resize(frame,(480,360))
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    roi_frame = 
