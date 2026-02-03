import cv2
import numpy as np

circle = np.zeros((512,512,3),np.uint8) + 255
cv2.circle(circle, (256,256), 60, (255,0,0), -1)

rectangle = np.zeros((512,512,3),np.uint8) + 255
cv2.rectangle(rectangle, (150,150), (350,350), (0,255,0), -1)

add = cv2.add(rectangle, circle) # Görüntü toplama işlemi

dst = cv2.addWeighted(circle,0.7, rectangle,0.3,0) # Ağırlıklı toplama işlemi



#cv2.imshow("Circle", circle)
#cv2.imshow("Rectangle", rectangle)
cv2.imshow("Added Image", add)
cv2.imshow("Weighted Image", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
