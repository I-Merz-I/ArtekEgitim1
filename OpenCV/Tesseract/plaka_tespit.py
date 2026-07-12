import os
import cv2
import numpy as np
import pytesseract
import imutils

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

if not os.path.exists(pytesseract.pytesseract.tesseract_cmd):
    raise FileNotFoundError("Tesseract bulunamadı. Kurulu yolu kontrol edin.")

img = cv2.imread(r"C:\Users\Muharrem\Documents\GitHub\ArtekEgitim1\OpenCV\Tesseract\licence_plate.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
filtered = cv2.bilateralFilter(gray,5,200,200)
edged = cv2.Canny(filtered,10,300)

contours = cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(contours)
cnts = sorted(cnts,key = cv2.contourArea, reverse=True)[:10]

screen = None

for x in cnts:
    epsilon = 0.018*cv2.arcLength(x,True)
    approx = cv2.approxPolyDP(x,epsilon,True)
    if len(approx) == 4:
        screen = approx
        break

mask = np.zeros(gray.shape,np.uint8)
new_img = cv2.drawContours(mask,[screen],0,(255,255,255),-1)
new_img = cv2.bitwise_and(img,img,mask = mask)

(x,y) = np.where(mask==255)
(topx,topy) = (np.min(x),np.min(y))
(bottomx,bottomy) = (np.max(x),np.max(y))

cropped = gray[topx:bottomx+1,topy:bottomy+1]

text = pytesseract.image_to_string(cropped,lang="eng")
print(text)

cv2.waitKey(0)
cv2.destroyAllWindows