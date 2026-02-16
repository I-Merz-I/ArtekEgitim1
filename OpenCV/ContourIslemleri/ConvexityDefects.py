import cv2

# Resmi yükle
img = cv2.imread("star.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# --- DÜZELTME 1: THRESH_BINARY_INV kullanıyoruz ---
# Arka plan beyaz olduğu için, "Ters" threshold yaparak arka planı siyah,
# yıldız çizgilerini beyaz yapıyoruz.
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Sadece dış hatları bul (RETR_EXTERNAL)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(contours) > 0:
    # --- DÜZELTME 2: En büyük konturu (yıldızı) seç ---
    cnt = max(contours, key=cv2.contourArea)

    hull = cv2.convexHull(cnt, returnPoints=False)
    defects = cv2.convexityDefects(cnt, hull)

    if defects is not None:
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])
            
            # Çizgileri çiz
            cv2.line(img, start, end, [0, 255, 0], 2)
            # Girinti noktasına kırmızı nokta koy
            cv2.circle(img, far, 5, [0, 0, 255], -1)

    cv2.imshow("Defects", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Kontur bulunamadı.")