import cv2
import numpy as np

# Kendi video yolunu buraya yazmalısın
video_path = r"C:\Users\Muharrem\Documents\GitHub\ArtekEgitim1\OpenCV\Alistirmalar\image_video\266987_tiny.mp4"
vid = cv2.VideoCapture(video_path)

backsub = cv2.createBackgroundSubtractorMOG2()

c = 0
counted_cars = [] 

while True:
    ret, frame = vid.read()
    if not ret:
        break

    fgmask = backsub.apply(frame)

    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)))
    fgmask = cv2.dilate(fgmask, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)), iterations=1)

    h, w = frame.shape[:2]

    line_y1 = h // 2 - 15  
    line_y2 = h // 2 + 15  

    cv2.line(frame, (0, line_y1), (w, line_y1), (0, 255, 0), 2)
    cv2.line(frame, (0, line_y2), (w, line_y2), (0, 255, 0), 2)

    contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    try: 
        hierarchy = hierarchy[0]
    except: 
        hierarchy = []

    # --- YENİ DURUM KONTROLÜ (STATE CHECK) ---
    # Başlangıçta bölgenin boş olduğunu varsayıyoruz
    car_in_zone_this_frame = False

    for contour, hier in zip(contours, hierarchy):
        (x, y, w_box, h_box) = cv2.boundingRect(contour)

        if w_box > 15 and h_box > 15:
            
            cv2.rectangle(frame, (x, y), (x + w_box, y + h_box), (255, 0, 0), 3)

            center_x = x + w_box // 2
            center_y = y + h_box // 2
            
            cv2.circle(frame, (center_x, center_y), 4, (0, 0, 255), -1)

            # Eğer herhangi bir araç çizgilerin arasına girdiyse:
            if line_y1 < center_y < line_y2:
                car_in_zone_this_frame = True # "Bölge dolu" bayrağını kaldır
                already_counted = False
                
                # Hafızadaki koordinatlarla karşılaştır
                for (cx, cy) in counted_cars:
                    if abs(center_x - cx) < 40 and abs(center_y - cy) < 40:
                        already_counted = True
                        break
                
                # Eğer yeni bir araçsa say
                if not already_counted:
                    c += 1 
                    counted_cars.append((center_x, center_y)) 

    # --- HAFIZA TEMİZLEME (MEMORY FLUSH) ---
    # Eğer taradığımız karede (frame) çizgiler arasında HİÇ araç yoksa, listeyi temizle.
    # Böylece arkadan gelen yeni araçlar, önceki araçların hayalet koordinatlarına takılmaz.
    if not car_in_zone_this_frame:
        counted_cars.clear()

    cv2.putText(frame, "Car: " + str(c), (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3, cv2.LINE_AA)
    
    cv2.imshow("Car Counting", frame)
    cv2.imshow("fgmask", fgmask)
    
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()