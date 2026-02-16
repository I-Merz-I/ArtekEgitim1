import cv2

img =cv2.imread("contour1.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours,_= cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img,contours,-1,(0,255,0),3)

cnt = contours[0]
area = cv2.contourArea(cnt) #konturun alanını verir

print("Area:",area)

perimeter = cv2.arcLength(cnt,True) #konturun çevresini verir
print("Perimeter:",perimeter)

cv2.imshow("Contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
