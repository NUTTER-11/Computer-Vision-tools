
import cv2
import mediapipe as mp
import time #to chec the frame rate
class handDetector():
    def __init__(self,mode=False,maxHands=2,detectionCon=0.5,trackCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon=trackCon


        self.mpHands=mp.solutions.hands
        self.hands=self.mpHands.Hands(self.mode,self.maxHands,self.detectionCon,self.trackCon)
        self.mpDraw=mp.solutions.drawing_utils


    def findHands(self,img,draw=True):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#HANDS ONLY USES RGB IMAGES SO THERE IS NEED OF CONVERSION OF THAT
        results=self.hands.process(imgRGB)
        #print(results.multi_hand_landmarks)#detects the coordinates of hands
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)
        return img

    def findPositions(self,img,handNo=0,draw=True):
        lnList=[]
        if self.results.multi_hand_landmarks:
            myHand=self.results.multi_hand_landmarks[handNo]
            for id,lm in enumerate(myHand.landmark):
                    h,w,c=img.shape
                    cx,cy=int(lm.x*w),int(lm.y*h)
                    print(id,cx,cy)
                    lmList.append([id,cx,cy])
                    if draw:
                        cv2.circle(img,(cx,cy),15,(255,0,255,cv2.FILLED))

        return lnList

def main():
    pTime=0
    cTime=0
    cap=cv2.VideoCapture(1)
    detector=handDetector()
    while True:
        success,img =cap.read()
        img=detector.findHands(img)
        lmList=detector.findPosition(img)
        cTime=time.time()

    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,
    (255,0,255),3)

    cv2.imshow('image',img)
    cv2.waitKey(1)
if __name__ == '__main__':
    main()
