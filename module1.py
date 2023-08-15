import  cv2
import mediapipe as mp
import time
cap =cv2.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpdraw=mp.solutions.drawing_utils
ptime=0
ctime=0

while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    RESULT=hands.process(imgRGB)
    print(RESULT.multi_hand_landmarks)
    if RESULT.multi_hand_landmarks:
        for handlms in RESULT.multi_hand_landmarks:
            mpdraw.draw_landmarks(img,handlms,mpHands.HAND_CONNECTIONS)

    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,
    (255,0,255),3)

    cv2.imshow('Detection',img)
    if cv2.waitKey(20) & 0xFF==ord('d'):#if letter  d is pressed stop video
        break
    cv2.waitKey(1)