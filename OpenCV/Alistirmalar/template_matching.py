import cv2
import numpy as np

image_path = r"C:\Users\Muharrem\Documents\GitHub\ArtekEgitim1\OpenCV\Alistirmalar\image_video\pexels-rickyrecap-3041347.jpg"
template_path = r"C:\Users\Muharrem\Documents\GitHub\ArtekEgitim1\OpenCV\Alistirmalar\image_video\pexels-rickyrecap-3041347k.jpg"

image = cv2.imread(image_path)
template = cv2.imread(template_path)

if image is None or template is None:
    raise FileNotFoundError("Görüntü veya şablon dosyası bulunamadı.")

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

w, h = template_gray.shape[::-1]
result = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)
locations = np.where(result >= 0.8)

for pt in zip(*locations[::-1]):
    cv2.rectangle(image,pt,(pt[0]+w,pt[1]+h),(0,255,0),3)

cv2.imshow("Detected", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

 