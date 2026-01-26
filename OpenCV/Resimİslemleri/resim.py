import cv2

def resizeWithAspectRatio(img, width = None, height = None, inter = cv2.INTER_AREA):
    
    dimension = None
    (h,w) = img.shape[:2]

    if width is None and height is None:
        return img
    if width is None:
        r = height / float(h)
        dimension = (int(w*r), height)
    else:
        r = width / float(w)
        dimension = (width, int(h*r))

    return cv2.resize(img, dimension, interpolation = inter)


img = cv2.imread("klon.jpg")
img1 = resizeWithAspectRatio(img, width = 300, height = None, inter = cv2.INTER_AREA)

cv2.imshow("Original", img)
cv2.imshow("Resized", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

img = cv2.imread("klon.jpg") #resmi yükle ve değişkene ata ve oku 

cv2.namedWindow("Image",cv2.WINDOW_NORMAL) #pencere oluşturma ve pencere boyutunu ayarlama

img = cv2.resize(img,(640, 480)) #resmi yeniden boyutlandırma

cv2.imshow("Image",img) #resmi ekranda gösterme
cv2.imwrite("klon1.jpg",img) #resmi kaydetme
cv2.waitKey(0)  #bir tuşa basılmasını bekle 
cv2.destroyAllWindows() #tüm pencereleri kapat


"""


