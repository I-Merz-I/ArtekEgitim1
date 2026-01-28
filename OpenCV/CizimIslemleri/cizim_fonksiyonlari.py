import cv2
import numpy as np

canvas = np.zeros((512,512,3),dtype="uint8")+255 # ile beyaz zemin yapilir


cv2.line(canvas,(50,50),(512,512),(150,25,15),thickness=20)
cv2.line(canvas,(512,10),(50,510),(15,25,150),thickness=10)

cv2.rectangle(canvas,(150,150),(250,250),(150,150,150),thickness=-1) # thickness -1 yapilirsa dolu sekilde cizilir

cv2.circle(canvas,(256,256),100,(25,45,56),thickness=-1)

cv2.putText(canvas,"BJK",(150,450),cv2.FONT_HERSHEY_TRIPLEX,5,(0,0,0),thickness=5,lineType=cv2.LINE_AA)

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
