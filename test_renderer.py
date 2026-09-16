import cv2
import os

from hand_tracker import HandTracker
from renderer import Renderer

# -------------------------------

print("Current Working Directory:")
print(os.getcwd())

image_path = os.path.join("assets", "magic_circle.png")

print("Looking for:", image_path)
print("Exists:", os.path.exists(image_path))

magic = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

if magic is None:
    print("\n❌ ERROR: Unable to load magic_circle.png")
    print("Please check the filename and location.")
    exit()

print("✅ Image Loaded Successfully")
print("Image Shape:", magic.shape)

# -------------------------------

tracker = HandTracker()
renderer = Renderer()

cap = cv2.VideoCapture(0)

WINDOW = "Magic Circle Test"

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

        # Palm center (MediaPipe landmark 9)
        palm = hands[0][9]

        cv2.circle(frame, palm, 6, (0, 0, 255), -1)

        renderer.draw_magic_circle(
            frame,
            magic,
            palm,
            220
        )

    cv2.imshow(WINDOW, frame)

    if cv2.getWindowProperty(WINDOW, cv2.WND_PROP_VISIBLE) < 1:
        break

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q") or key == ord("Q") or key == 27:
        break

tracker.close()

cap.release()

cv2.destroyAllWindows()