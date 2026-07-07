import cv2 

img = cv2.imread(r"C:\Users\Muharrem\Documents\GitHub\ArtekEgitim1\OpenCV\YuzAlgilama\De9RcV3X0AEP989.jpg")
face_cascade = cv2.CascadeClassifier(r"C:\Users\Muharrem\Downloads\haarcascade_frontalface_alt.xml")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.3,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Face Detection", img)
cv2.waitKey(0)


    
