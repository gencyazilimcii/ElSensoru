import cv2
import time
import os
import HandTrackingMadule as htm

wCam,hCam=1250,700

cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

folderPath="FingerImages"

myList=os.listdir(folderPath)
print(myList)
overlayList=[]


for imPath in myList:
    image=cv2.imread(f'{folderPath}/{imPath}')
    #print(f'{folderPath}/{imPath}')
    overlayList.append(image)


print(len(overlayList))   
pTime=0

detector=htm.handDetector(detectionCon=0.75)
tipIds=[4,8,12,16,20]

while True:
    success,img=cap.read()
    
    imgg=detector.findHands(img)
    lmlist=detector.findPosition(imgg,draw=False)
    #print(lmlist)
    if len(lmlist)!=0:
        fingers=[]
        #thumb baş parmak
        if lmlist[tipIds[0]][1]>lmlist[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # diğer 4 parmak
        for id in range(1,5):
            if lmlist[tipIds[id]][2]<lmlist[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        #print(fingers)
        totalFingers=fingers.count(1 )
        print(totalFingers)
    


        h,w,c=overlayList[totalFingers-1].shape
    
        img[0:h,0:w] =overlayList[totalFingers-1]
    cTime=time.time()
    fps=1/(cTime-pTime)

    pTime=cTime
    cv2.putText(img,f'Fps:{int(fps)}',(400,70),cv2.FONT_HERSHEY_PLAIN ,3,(255,0,0),3)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
    
  
