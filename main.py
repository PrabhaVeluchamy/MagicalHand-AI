import cv2
import time

from hand_tracker import HandTracker
from game import MagicGame


def main():

    print("=" * 60)
    print("        MagicHandsAI v2.0")
    print("=" * 60)
    print("Starting Camera...")
    print()

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Unable to open webcam.")
        return

    # Camera Settings
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)

    tracker = HandTracker(
        max_hands=2,
        detection_confidence=0.5,
        tracking_confidence=0.5
    )

    game = MagicGame()

    frame_count = 0
    fps = 0
    prev_time = time.time()

    print("MagicHandsAI Started Successfully")
    print()
    print("Controls")
    print("--------------------------------")
    print("H   -> Toggle HUD")
    print("C   -> Clear Particles")
    print("R   -> Recording (Future)")
    print("S   -> Screenshot (Future)")
    print("ESC -> Exit")
    print("--------------------------------")

    while True:

        success, frame = cap.read()

        if not success:
            break

        # Mirror View
        frame = cv2.flip(frame, 1)

        frame_count += 1

        # Process every second frame for better FPS
        if frame_count % 2 == 0:
            tracker.process(frame)

        # Draw Hand Landmarks
        tracker.draw(frame)

        # Get Hand Landmarks
        hands = tracker.get_landmarks(frame)

        # Update Game
        game.update(frame, hands)

        # FPS
        current = time.time()

        fps = 1 / (current - prev_time)

        prev_time = current

        cv2.putText(
            frame,
            f"FPS : {int(fps)}",
            (520, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        cv2.imshow("MagicHandsAI v2.0", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == 27:
            break

        game.handle_key(key)

    print("Closing MagicHandsAI...")

    game.close()
    tracker.close()

    cap.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()