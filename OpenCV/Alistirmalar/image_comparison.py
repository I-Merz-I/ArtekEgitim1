import cv2
import numpy as np


path = "C:\\Users\\Muharrem\\Documents\\GitHub\\ArtekEgitim1\\OpenCV\\Alistirmalar\\pexels-matthardy-2658450.jpg"
path2 = "C:\\Users\\Muharrem\\Documents\\GitHub\\ArtekEgitim1\\OpenCV\\Alistirmalar\\pexels-rickyrecap-3041347.jpg"
img1 = cv2.imread(path)
img1 = cv2.resize(img1, (500, 500))

img2 = cv2.imread(path2)
img2 = cv2.resize(img2, (500, 500))

if img1.shape == img2.shape:
    diff = cv2.subtract(img1,img2)
    cv2.imshow("Difference", diff)
    b, g, r = cv2.split(diff)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("The images are the same")
    else:
        print("The images are different")

cv2.imshow("Image", img1)
cv2.imshow("Image2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
