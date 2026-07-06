import cv2 
def nothing(x):
    pass

img1 = cv2.imread(r"C:\Users\Muharrem\Documents\GitHub\ArtekEgitim1\OpenCV\Alistirmalar\image_video\fakili.jpg")
img1 = cv2.resize(img1, (600, 400))
img2 = cv2.imread(r"C:\Users\Muharrem\Documents\GitHub\ArtekEgitim1\OpenCV\Alistirmalar\image_video\trossard.jpg")
img2 = cv2.resize(img2, (600, 400))

output = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
window_name = "Image Transition"
cv2.namedWindow(window_name)

cv2.createTrackbar("Alpha-Beta", window_name, 0, 1000, nothing)

while True:
    cv2.imshow(window_name, output)
    alpha = cv2.getTrackbarPos("Alpha-Beta", window_name) / 1000
    beta = 1 - alpha
    output = cv2.addWeighted(img1, alpha, img2, beta, 0)
    print(f"Alpha: {alpha}, Beta: {beta}")

    key = cv2.waitKey(30) & 0xFF
    if key == 27:  # ESC to exit
        break

cv2.destroyAllWindows()

    