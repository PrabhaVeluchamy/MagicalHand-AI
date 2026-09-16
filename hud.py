import cv2
import time


class HUD:

    def __init__(self):

        self.last_time = time.time()
        self.fps = 0

        self.health = 100
        self.mana = 100

    # ---------------------------------
    # FPS
    # ---------------------------------

    def update_fps(self):

        current = time.time()

        dt = current - self.last_time

        if dt > 0:
            self.fps = int(1 / dt)

        self.last_time = current

    # ---------------------------------
    # Health Bar
    # ---------------------------------

    def draw_health(self, frame):

        x = 20
        y = 45
        w = 220
        h = 20

        cv2.rectangle(frame, (x, y), (x + w, y + h), (70, 70, 70), 2)

        value = int((self.health / 100) * w)

        cv2.rectangle(
            frame,
            (x, y),
            (x + value, y + h),
            (0, 0, 255),
            -1
        )

        cv2.putText(
            frame,
            "Health",
            (x, y - 8),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            1
        )

    # ---------------------------------
    # Mana Bar
    # ---------------------------------

    def draw_mana(self, frame):

        x = 20
        y = 80
        w = 220
        h = 20

        cv2.rectangle(frame, (x, y), (x + w, y + h), (70, 70, 70), 2)

        value = int((self.mana / 100) * w)

        cv2.rectangle(
            frame,
            (x, y),
            (x + value, y + h),
            (255, 120, 0),
            -1
        )

        cv2.putText(
            frame,
            "Mana",
            (x, y - 8),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            1
        )

    # ---------------------------------
    # Draw HUD
    # ---------------------------------

    def draw(self, frame, spell, hand_count=0):

        self.update_fps()

        cv2.putText(
            frame,
            "MagicHandsAI v2.0",
            (20, 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 220, 255),
            2
        )

        self.draw_health(frame)
        self.draw_mana(frame)

        cv2.putText(
            frame,
            f"Spell : {spell}",
            (20, 130),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            f"Hands : {hand_count}",
            (20, 160),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 255),
            2
        )

        cv2.putText(
            frame,
            f"FPS : {self.fps}",
            (20, 190),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "ESC - Exit",
            (20, frame.shape[0] - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (180, 180, 180),
            1
        )