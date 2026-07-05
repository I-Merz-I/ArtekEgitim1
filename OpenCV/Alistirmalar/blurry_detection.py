import cv2

img = cv2.imread("C:\\Users\\Muharrem\\Documents\\GitHub\\ArtekEgitim1\\OpenCV\\Alistirmalar\\image_video\\images.jpg")

laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian_var = laplacian.var()
print("Laplacian Variance:", laplacian_var)

if laplacian_var < 100:
    print("The image is blurry")
else:
    print("The image is not blurry")