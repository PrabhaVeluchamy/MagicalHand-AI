import cv2
import math


class Portal:

    def __init__(self):

        self.angle = 0

    # -----------------------------------
    # Draw Portal
    # -----------------------------------

    def draw(self, frame, center, radius):

        self.angle = (self.angle + 4) % 360

        overlay = frame.copy()

        # ==========================
        # Outer Glow
        # ==========================

        cv2.circle(
            overlay,
            center,
            radius + 12,
            (0, 120, 255),
            3,
            cv2.LINE_AA
        )

        cv2.circle(
            overlay,
            center,
            radius,
            (0, 180, 255),
            4,
            cv2.LINE_AA
        )

        # ==========================
        # Inner Ring
        # ==========================

        cv2.circle(
            overlay,
            center,
            int(radius * 0.72),
            (0, 255, 255),
            2,
            cv2.LINE_AA
        )

        # ==========================
        # Rotating Energy Lines
        # ==========================

        for i in range(16):

            theta = math.radians(
                i * 22.5 + self.angle
            )

            x1 = int(
                center[0] +
                math.cos(theta) * radius
            )

            y1 = int(
                center[1] +
                math.sin(theta) * radius
            )

            x2 = int(
                center[0] +
                math.cos(theta) * (radius - 20)
            )

            y2 = int(
                center[1] +
                math.sin(theta) * (radius - 20)
            )

            cv2.line(
                overlay,
                (x1, y1),
                (x2, y2),
                (0, 255, 255),
                2,
                cv2.LINE_AA
            )

        # ==========================
        # Orbiting Sparks
        # ==========================

        for i in range(8):

            theta = math.radians(
                self.angle * 2 + i * 45
            )

            x = int(
                center[0] +
                math.cos(theta) *
                (radius - 10)
            )

            y = int(
                center[1] +
                math.sin(theta) *
                (radius - 10)
            )

            cv2.circle(
                overlay,
                (x, y),
                3,
                (255, 255, 255),
                -1,
                cv2.LINE_AA
            )

        # ==========================
        # Center Glow
        # ==========================

        cv2.circle(
            overlay,
            center,
            10,
            (0, 255, 255),
            -1,
            cv2.LINE_AA
        )

        # ==========================
        # Blend
        # ==========================

        cv2.addWeighted(
            overlay,
            0.35,
            frame,
            0.65,
            0,
            frame
        )