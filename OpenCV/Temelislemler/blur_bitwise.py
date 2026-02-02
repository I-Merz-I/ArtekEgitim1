import cv2
import numpy as np

img1 = cv2.imread("image1.png")
img2 = cv2.imread("image2.png")

bit_and = cv2.bitwise_and(img1, img2)
bit_or = cv2.bitwise_or(img1, img2)
bit_xor = cv2.bitwise_xor(img1, img2)
bit_not = cv2.bitwise_not(img1)
bit_not2 = cv2.bitwise_not(img2)

cv2.imshow("Bitwise AND", bit_and)
cv2.imshow("Bitwise OR", bit_or)
cv2.imshow("Bitwise XOR", bit_xor)
cv2.imshow("Bitwise NOT Image 1", bit_not)
cv2.imshow("Bitwise NOT Image 2", bit_not2)


# blurred_img = cv2.blur(img1, (15, 15), 0)

# cv2.imshow("Blurred Image", blurred_img)
# cv2.imshow("Image 1", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()

