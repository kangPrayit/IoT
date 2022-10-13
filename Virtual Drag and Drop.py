import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cap.read()
    # hands, img = detector.findHands(img)
    hands = detector.findHands(img, draw=False)

    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        fingers = detector.fingersUp(hand)
        length, info, img = detector.findDistance(lmList[4], lmList[8], img)
        print(length, info)


    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    # untuk keluar tekan tombol q
    if key == ord('q'):
        break