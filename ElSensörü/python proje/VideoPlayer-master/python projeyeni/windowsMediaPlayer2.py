import numpy as np
import cv2
cap = cv2.VideoCapture('FingerImages/ASD.mp4') # Kullanacağınız videonun adını buraya yazmalısınız!!

while(cap.isOpened()):
#Çerçeveler halinde görüntü yakalar
    ret, frame = cap.read()

#Üzerinde işlem yapacağımız çerçeve buraya gelsin ve griye dönsün
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#Sonuç Çerçeveyi Görüntüleme:
    cv2.imshow('frame',gray)
    if cv2.waitKey(25) & 0xFF == ord('q'):
       break

#Herşey yolunda gitti ise dükkanı kapatabiliriz :)
cap.release()
cv2.destroyAllWindows()