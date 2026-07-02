import cv2 
import numpy as np

def findMaxContour(contours):
    # Gelen tüm konturlar içinde en büyük alanlı konturu seç
    # Böylece maskenin içindeki küçük lekeler değil, en büyük yüz bölgesi kullanılır.
    if not contours:
        return None

    max_contour = None
    max_area = 0

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            max_contour = contour

    return max_contour


cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    height, width = frame.shape[:2]
    rect_w = int(width * 0.4)
    rect_h = int(height * 0.65)
    x1 = (width - rect_w) // 2
    y1 = (height - rect_h) // 2
    x2 = x1 + rect_w
    y2 = y1 + rect_h

    roi = frame[y1:y2, x1:x2]

    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # ROI'yu çerçevele
    roi_blur = cv2.GaussianBlur(roi, (5, 5), 0)  # yüz maskesi için gürültüyü azalt
    ycrcb = cv2.cvtColor(roi_blur, cv2.COLOR_BGR2YCrCb)  # HSV yerine YCrCb ile daha güvenli ten rengi tespiti

    # Bu aralık yüzün koyu ve aydınlık tonları için genişleyebilecek Cr/Cb değerleri içerir.
    # Y kanalı 0-255 arasında olduğu için sadece Cr/Cb'ye odaklandık.
    lower_skin = np.array([0, 133, 77], dtype=np.uint8)
    upper_skin = np.array([255, 173, 127], dtype=np.uint8)

    mask = cv2.inRange(ycrcb, lower_skin, upper_skin)  # YCrCb uzayında ten rengi maskesi oluştur
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)  # küçük gürültü lekelerini sil
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)  # maskeyi düzgün bir yüz bölgesine kapat

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # kontur bul

    if len(contours) > 0:
        c = findMaxContour(contours)  # en büyük ve en anlamlı konturu al
        if c is not None and len(c) >= 5:
            # Konturdan direkt noktayı almak yerine convex hull kullanmak
            # yanlış iç boşlukları veya garip kontur hatalarını azaltır.
            hull = cv2.convexHull(c)
            extL = tuple(hull[hull[:, :, 0].argmin()][0])  # en sol noktayı al
            extR = tuple(hull[hull[:, :, 0].argmax()][0])  # en sağ noktayı al
            extT = tuple(hull[hull[:, :, 1].argmin()][0])  # en üst noktayı al
            extB = tuple(hull[hull[:, :, 1].argmax()][0])  # en alt noktayı al

            cv2.circle(roi, extL, 8, (0, 0, 255), -1)  # en sol noktayı işaretle
            cv2.circle(roi, extR, 8, (0, 0, 255), -1)  # en sağ noktayı işaretle
            cv2.circle(roi, extT, 8, (0, 0, 255), -1)  # en üst noktayı işaretle
            cv2.circle(roi, extB, 8, (0, 0, 255), -1)  # en alt noktayı işaretle

            cv2.line(roi, extL, extR, (255, 0, 0), 2)  # en sol ve en sağ noktayı birleştir
            cv2.line(roi, extT, extB, (255, 0, 0), 2)  # en üst ve en alt noktayı birleştir

    cv2.imshow("Mask", mask)
    cv2.imshow("Video", frame)
    cv2.imshow("ROI", roi)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()