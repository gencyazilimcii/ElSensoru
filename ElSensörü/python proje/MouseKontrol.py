import cv2
import numpy as np
import HandTrackingMadule as htm
import time
import autopy


wCam,hCam=640,480



cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime=0
detector=htm.handDetector(maxHands=2)

while True:
    # 1. find hand landmarks
  
    success,img=cap.read()
    
    imgg=detector.findHands(img)
    lmlist=detector.findPosition(imgg,draw=False)
     
   

 
    
    # 2.Get the tip of the index and middle fingers
    if len(lmlist)!=0:
        x1,y1=lmlist[8][1:]
        x2,y2=lmlist[12][1:]
        print(x1,y1,x2,y2) 
    # 3. check which fingers are up
    fingers=detector.fingersUp()
    print(fingers)
    # 4.only Index finger: Moving Mode
    # 5. Convert Coordicates
    #6. smoothen values
    #7.move mouse
    #8.Both index and middle fingers are up:clicking mode
    #9.find distance between fingers
    #10.click mouse if distance short
    #11.frame Rate
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    #12.Display


    cv2.imshow("Image",img)
    cv2.waitKey(1)

