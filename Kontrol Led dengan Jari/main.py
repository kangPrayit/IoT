from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cap.read()
    hand, img = detector.findHands(img)
    if hand:
        lmList = hand[0]["lmList"]
        # print(lmList)
        fingers = detector.fingersUp(hand[0])
        print(fingers)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key==ord("q"):
        break

cv2.destroyAllWindows()