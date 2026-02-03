import cv2
import numpy as np
import matplotlib.pyplot as plt

#cv2.Canny(input,threshold1,threshold2)

cap = cv2.VideoCapture(0)

while True:
    
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)

    edges = cv2.Canny(frame,100,200)

    cv2.imshow("Orijinal",frame)
    cv2.imshow("Kenarlar",edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




""" görüntü köse saptama


img = cv2.imread("klon.jpg")
cv2.imshow("img",img)


b,c,r = cv2.split(img)

plt.hist(b.ravel(),256,[0,256])
plt.hist(c.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
"""