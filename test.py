import cv2

from hand_tracker import HandTracker
from gesture import GestureDetector

cap = cv2.VideoCapture(0)

tracker = HandTracker()
gesture = GestureDetector()

WINDOW = "Gesture Test"

cv2.namedWindow(WINDOW)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    tracker.process(frame)
    tracker.draw(frame)

    hands = tracker.get_landmarks(frame)

    if len(hands) > 0:

        state = gesture.get_hand_state(hands[0])

        dist = gesture.get_pinch_distance(hands[0])

        cv2.putText(
            frame,
            f"Gesture : {state}",
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

        cv2.putText(
            frame,
            f"Distance : {dist}",
            (20,80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255,255,255),
            2
        )

    cv2.imshow(WINDOW, frame)

    if cv2.getWindowProperty(WINDOW, cv2.WND_PROP_VISIBLE) < 1:
        break

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q") or key == 27:
        break

tracker.close()
cap.release()
cv2.destroyAllWindows()
