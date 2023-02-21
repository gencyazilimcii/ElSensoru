import time
import vlc

G=vlc.MediaPlayer('FingerImages/ASD.mp4')
G.play()
time.sleep()
G.stop()