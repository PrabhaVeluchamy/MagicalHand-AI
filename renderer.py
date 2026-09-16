import cv2
import numpy as np


class Renderer:

    def __init__(self):

        self.outer_angle = 0
        self.inner_angle = 0

        self.cached_outer = None
        self.cached_inner = None

        self.last_size = 0
        self.frame = 0

    # --------------------------------------------------
    # Rotate Image
    # --------------------------------------------------

    def rotate(self, image, angle):

        h, w = image.shape[:2]

        matrix = cv2.getRotationMatrix2D(
            (w // 2, h // 2),
            angle,
            1.0
        )

        return cv2.warpAffine(
            image,
            matrix,
            (w, h),
            flags=cv2.INTER_LINEAR,
            borderMode=cv2.BORDER_TRANSPARENT
        )

    # --------------------------------------------------
    # Overlay PNG (RGBA)
    # --------------------------------------------------

    def overlay(self, frame, overlay, x, y):

        if overlay is None:
            return

        if overlay.shape[2] != 4:
            return

        h, w = overlay.shape[:2]

        if x < 0 or y < 0:
            return

        if x + w > frame.shape[1]:
            return

        if y + h > frame.shape[0]:
            return

        alpha = overlay[:, :, 3] / 255.0

        roi = frame[y:y+h, x:x+w]

        for c in range(3):
            roi[:, :, c] = (
                alpha * overlay[:, :, c]
                + (1 - alpha) * roi[:, :, c]
            )

        frame[y:y+h, x:x+w] = roi

    # --------------------------------------------------
    # Glow Effect
    # --------------------------------------------------

    def glow(self, frame, center, radius):

        overlay = frame.copy()

        cv2.circle(
            overlay,
            center,
            radius,
            (0, 180, 255),
            -1,
            cv2.LINE_AA
        )

        cv2.addWeighted(
            overlay,
            0.12,
            frame,
            0.88,
            0,
            frame
        )

    # --------------------------------------------------
    # Draw Magic Circle
    # --------------------------------------------------

    def draw_magic_circle(self, frame, image, center, size):

        if image is None:
            return

        self.frame += 1

        self.outer_angle = (self.outer_angle + 2) % 360
        self.inner_angle = (self.inner_angle - 3) % 360

        if (
            self.cached_outer is None
            or self.last_size != size
            or self.frame % 3 == 0
        ):

            outer = cv2.resize(
                image,
                (size, size)
            )

            inner_size = int(size * 0.7)

            inner = cv2.resize(
                image,
                (inner_size, inner_size)
            )

            self.cached_outer = self.rotate(
                outer,
                self.outer_angle
            )

            self.cached_inner = self.rotate(
                inner,
                self.inner_angle
            )

            self.last_size = size

        self.glow(
            frame,
            center,
            size // 2
        )

        x = center[0] - size // 2
        y = center[1] - size // 2

        self.overlay(
            frame,
            self.cached_outer,
            x,
            y
        )

        inner_size = int(size * 0.7)

        x2 = center[0] - inner_size // 2
        y2 = center[1] - inner_size // 2

        self.overlay(
            frame,
            self.cached_inner,
            x2,
            y2
        )





        