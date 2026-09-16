import cv2
import math


class SpellWheel:

    def __init__(self):

        self.spells = [
            "MAGIC",
            "FIREBALL",
            "LASER",
            "SHIELD"
        ]

        self.selected = 0

    def draw(self, frame, center):

        radius = 120

        cx, cy = center

        cv2.circle(
            frame,
            center,
            radius,
            (0, 180, 255),
            2,
            cv2.LINE_AA
        )

        for i, spell in enumerate(self.spells):

            angle = math.radians(i * 90 - 90)

            x = int(cx + radius * math.cos(angle))
            y = int(cy + radius * math.sin(angle))

            color = (
                (0, 255, 255)
                if i == self.selected
                else (255, 255, 255)
            )

            cv2.circle(
                frame,
                (x, y),
                22,
                color,
                -1,
                cv2.LINE_AA
            )

            cv2.putText(
                frame,
                spell[0],
                (x - 8, y + 8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 0),
                2
            )

    def update_selection(self, index):

        if 0 <= index < len(self.spells):
            self.selected = index

    def current_spell(self):
        return self.spells[self.selected]