import cv2
import mediapipe as mp
import time
cap=cv2.VideoCapture(0)
mpFaceDetection=mp.solutions.face_detection
facedetection=mpFaceDetection.FaceDetection()
mpDraw=mp.solutions.drawing_utils
pTime=0
while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=facedetection.process(imgRGB)
    print(results)
    if results.detections:
        for id,detection in enumerate(results.detections):
            mpDraw.draw_detection(img,detection)




    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,f'FPS:{int(fps)}',(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    cv2.imshow("face",img)
    cv2.waitKey(1)