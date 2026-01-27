import cv2
import numpy as np

path = "opencvlogo.png"
img = cv2.imread(path)

print(img.shape)  # Görüntünün boyutlarını yazdır (yükseklik, genişlik, kanal sayısı)

px = img[0,0]
#print(px)  # (B, G, R) değerlerini yazdır

