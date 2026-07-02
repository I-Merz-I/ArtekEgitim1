import cv2

vid = cv2.VideoCapture("C:\\Users\\Muharrem\\Documents\\GitHub\\ArtekEgitim1\\OpenCV\\Alistirmalar\\4101232-sd_640_338_25fps.mp4")

while True:
    ret,frame = vid.read()
    if not ret:
        break

    roi = frame[100:250, 150:550]  # Yüz bölgesini seçmek için ROI belirle
    rows,cols,_ = roi.shape # ROI'nun boyutlarını al

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)  # ROI'yu gri tonlamaya çevir
    gray = cv2.equalizeHist(gray)  # parlaklık farklarını dengeler
    _, threshold = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY_INV)  # daha net siyah göz bebeği maskesi

    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # sadece dış konturları al
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 60 or area > 1600:
            continue  # çok küçük/çok büyük konturları at
        (x, y, w, h) = cv2.boundingRect(cnt)  # Konturun etrafına dikdörtgen çiz
        ratio = w / float(h) if h else 0
        if ratio < 0.5 or ratio > 1.8:
            continue  # çok ince veya çok uzun alanları at

        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Konturun etrafına dikdörtgen çiz
        cv2.line(roi, (x + w // 2, 0), (x + w // 2, rows), (255, 0, 0), 2)  # orta çizgi
        cv2.line(roi, (0, y + h // 2), (cols, y + h // 2), (255, 0, 0), 2)  # orta çizgi


    cv2.imshow("Video", frame)
    cv2.imshow("ROI", roi)
    cv2.imshow("Threshold", threshold)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()