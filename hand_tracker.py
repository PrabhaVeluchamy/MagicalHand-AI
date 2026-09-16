import cv2
import mediapipe as mp
import math


class HandTracker:

    def __init__(
            self,
            max_hands=2,
            detection_confidence=0.5,
            tracking_confidence=0.5):

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(
            static_image_mode=False,
            max_num_hands=max_hands,
            model_complexity=0,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )

        self.drawer = mp.solutions.drawing_utils

        self.results = None

    # ---------------------------------
    # Process Frame
    # ---------------------------------

    def process(self, frame):

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        rgb.flags.writeable = False

        self.results = self.hands.process(rgb)

        rgb.flags.writeable = True

    # ---------------------------------
    # Draw Landmarks
    # ---------------------------------

    def draw(self, frame):

        if self.results is None:
            return

        if not self.results.multi_hand_landmarks:
            return

        for hand in self.results.multi_hand_landmarks:

            self.drawer.draw_landmarks(
                frame,
                hand,
                self.mpHands.HAND_CONNECTIONS
            )

    # ---------------------------------
    # Get Landmark List
    # ---------------------------------

    def get_landmarks(self, frame):

        hands = []

        if self.results is None:
            return hands

        if not self.results.multi_hand_landmarks:
            return hands

        h, w = frame.shape[:2]

        for hand in self.results.multi_hand_landmarks:

            pts = []

            for lm in hand.landmark:

                pts.append(
                    (
                        int(lm.x * w),
                        int(lm.y * h)
                    )
                )

            hands.append(pts)

        return hands

    # ---------------------------------
    # Hand Centers
    # ---------------------------------

    def get_hand_centers(self, frame):

        centers = []

        hands = self.get_landmarks(frame)

        for hand in hands:

            centers.append(hand[9])

        return centers

    # ---------------------------------
    # Distance
    # ---------------------------------

    def get_distance(self, p1, p2):

        return math.hypot(
            p1[0] - p2[0],
            p1[1] - p2[1]
        )

    # ---------------------------------
    # Close
    # ---------------------------------

    def close(self):

        self.hands.close()