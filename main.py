import cv2
from cvzone.HandTrackingModule import HandDetector

# Kamerayı aç
cap = cv2.VideoCapture(0)

# El algılayıcı
detector = HandDetector(
    staticMode=False,
    maxHands=1,
    detectionCon=0.7,
    minTrackCon=0.5
)

while True:
    success, img = cap.read()

    if not success:
        print("Camera could not be opened!")
        break

    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        total = fingers.count(1)

        cv2.putText(
            img,
            f"Fingers: {total}",
            (20, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            2,
            (0, 255, 0),
            3
        )

    cv2.imshow("Computer Vision - Finger Counter", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()