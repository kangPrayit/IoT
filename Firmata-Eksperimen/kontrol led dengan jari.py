from cvzone.HandTrackingModule import HandDetector
from pyfirmata import Arduino
import cv2

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

board = Arduino("COM4")

while True:
    success, img = cap.read()
    hand, img = detector.findHands(img)
    if hand:
        fingers = detector.fingersUp(hand[0])
    else:
        fingers = [0, 0, 0, 0, 0]
    board.digital[5].write(fingers[1])
    board.digital[6].write(fingers[2])
    board.digital[7].write(fingers[3])
    print(fingers)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
