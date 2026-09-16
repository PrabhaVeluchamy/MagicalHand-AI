import cv2
import numpy as np
import random


class EnergyBeam:

    def __init__(self):

        self.phase = 0

    def draw(self, frame, start, end):

        self.phase += 1

        start = np.array(start, dtype=np.float32)
        end = np.array(end, dtype=np.float32)

        distance = np.linalg.norm(end - start)

        if distance < 10:
            return

        direction = (end - start) / distance
        normal = np.array([-direction[1], direction[0]])

        points = []

        # Faster than 25 segments
        segments = 12

        for i in range(segments + 1):

            t = i / segments

            point = start + direction * distance * t

            if 0 < i < segments:
                point += normal * random.randint(-10, 10)

            points.append(tuple(point.astype(int)))

        overlay = frame.copy()

        # Glow
        cv2.polylines(
            overlay,
            [np.array(points)],
            False,
            (0, 170, 255),
            8,
            cv2.LINE_AA
        )

        cv2.addWeighted(
            overlay,
            0.25,
            frame,
            0.75,
            0,
            frame
        )

        # Main Beam
        cv2.polylines(
            frame,
            [np.array(points)],
            False,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )

        # Energy Balls
        for i in range(3):

            t = ((self.phase * 10) + i * 60) % distance

            p = start + direction * t

            cv2.circle(
                frame,
                tuple(p.astype(int)),
                5,
                (255, 255, 255),
                -1
            )

        # Random Sparks
        for _ in range(4):

            t = random.random()

            p = start + direction * distance * t

            p += normal * random.randint(-10, 10)

            cv2.circle(
                frame,
                tuple(p.astype(int)),
                2,
                (0, 255, 255),
                -1
            )