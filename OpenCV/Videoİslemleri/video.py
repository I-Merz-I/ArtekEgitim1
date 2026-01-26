import cv2

cap = cv2.VideoCapture(0) #kamerayı başlat
fileName = "./OpenCV/Videoİslemleri/video_output.avi" #kaydedilecek dosya adı
frameRate = 30.0  #frame rate belirleme
codec= cv2.VideoWriter_fourcc(*'XVID') #codec belirleme
resolution = (640,480) #çözünürlük belirleme
videoFileOutput = cv2.VideoWriter(fileName,codec,frameRate,resolution) #video dosyası oluşturma


while True:
    ret , frame = cap.read() #kameradan görüntü al
    videoFileOutput.write(frame) #görüntüyü dosyaya yaz

    cv2.imshow("Video", frame)  #görüntüyü ekranda göster

    if cv2.waitKey(1) & 0xFF == ord('q'): #q tuşuna basılınca çık
        break

videoFileOutput.release() #video dosyasını serbest bırak
cap.release() #kamerayı serbest bırak
cv2.destroyAllWindows() #tüm pencereleri kapat
