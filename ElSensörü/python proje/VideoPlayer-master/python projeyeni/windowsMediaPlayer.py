import cv2 
import vlc
g=vlc.MediaPlayer('FingerImages/ASD.mp4')
kamera=cv2.VideoCapture('FingerImages/ASD.mp4') # oynatılacak videoyu tanımlama
kamera.set(cv2.CAP_PROP_FRAME_WIDTH,640)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT,480) #­ Kamera Boyutlandırma
while True:
    ret,goruntu=kamera.read() # kamera okumayı başlatma
    cv2.imshow('goruntu',goruntu) # görüntüyü gösterme
    g.play()
              
    if cv2.waitKey(25) & 0xFF ==ord('t'): # t tuşuna basılınca durdur.
        break
 
kamera.release() # kamerayı serbest bırak.
cv2.destroyAllWindows() # açılan pencereleri kapat.