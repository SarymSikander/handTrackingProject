import math
import cv2
import time
import numpy
import numpy as np
import handTrackingModule as htm
import wmi # this library used to change brightness of ONLY windows interface

cap = cv2.VideoCapture(0)

pTime = 0

wCam, hCam = 680, 720
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.HandDetector(detectionCon=0.7)

w = wmi.WMI(namespace='wmi')
brightness = w.WmiMonitorBrightnessMethods()[0]
minBrt = 0
maxBrt = 100

brt = 0
brtBar = 400
brtPer = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # this flips the img horizontally bcs cv2 automatically flips the image, and it looks mirrored (and weird and creepy)
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:

        # position of tip of thumb and tip of index in hand landmarks
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        # middle of the line
        cx, cy = (x1+x2)//2, (y1+y2)//2

        # adding circles on the tip of thumb and index finger, then adding a line,
        # and then adding a small circle in the middle of the line
        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
        cv2.circle(img, (cx, cy), 8, (0, 0, 0), cv2.FILLED)

        length = math.hypot(x2-x1, y2-y1)

        brt = np.interp(length, [50, 200], [minBrt, maxBrt])
        brtBar = np.interp(length, [50, 200], [400, 150])
        brtPer = np.interp(length, [50, 200], [0, 100])
        brightness.WmiSetBrightness(brt, 0)

        if length < 50:
            cv2.circle(img, (cx, cy), 6, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 5)
    cv2.rectangle(img, (50, int(brtBar)), (85, 400), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'{int(brtPer)} %', (40, 450), cv2.FONT_HERSHEY_TRIPLEX, 1, (242, 20, 0), 3)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_TRIPLEX, 1, (242, 20, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
