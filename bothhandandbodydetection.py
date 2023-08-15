import cv2
import mediapipe as mp#
import time

mpPose=mp.solutions.pose#model created
pose=mpPose.Pose()#object created
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils


pTime=0
cap = cv2.VideoCapture(0)
while True:
    success,img =cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    RESULTS=pose.process(imgRGB)
    print(RESULTS.pose_landmarks)
    results=hands.process(imgRGB)
    print(results.multi_hand_landmarks)
    if  RESULTS.pose_landmarks:
        mpDraw.draw_landmarks(img,RESULTS.pose_landmarks,mpPose.POSE_CONNECTIONS)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)



    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow("pose",img)
    cv2.waitKey(1)
cap=cv2.VideoCapture(0)

mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils                #gives the pints on hand or drAW POINTS ON HAND


