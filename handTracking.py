import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()

    # converting the images that cv2 captures to RGB format bcs MediaPipe's hands.process() only accepts RGB images
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        # this for loop iterates through each hand
        for handLms in results.multi_hand_landmarks:
            # this for loop iterates through each landmark of each hand
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            # draws landmarks and connections around each hand
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # fps counter
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    # adding a small fps counter to the side of the screen
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (49, 16, 71), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
