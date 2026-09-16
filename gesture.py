import math


class GestureDetector:

    def __init__(self):

        self.THUMB_TIP = 4
        self.INDEX_TIP = 8
        self.MIDDLE_TIP = 12
        self.RING_TIP = 16
        self.PINKY_TIP = 20

    # ------------------------------------
    # Distance Between Two Points
    # ------------------------------------

    def distance(self, p1, p2):

        return math.hypot(
            p1[0] - p2[0],
            p1[1] - p2[1]
        )

    # ------------------------------------
    # Finger States
    # Returns:
    # Thumb, Index, Middle, Ring, Pinky
    # ------------------------------------

    def finger_states(self, hand):

        thumb = hand[self.THUMB_TIP][0] > hand[3][0]

        index = hand[self.INDEX_TIP][1] < hand[6][1]

        middle = hand[self.MIDDLE_TIP][1] < hand[10][1]

        ring = hand[self.RING_TIP][1] < hand[14][1]

        pinky = hand[self.PINKY_TIP][1] < hand[18][1]

        return (
            thumb,
            index,
            middle,
            ring,
            pinky
        )

    # ------------------------------------
    # Pinch Detection
    # ------------------------------------

    def is_pinching(self, hand):

        thumb = hand[self.THUMB_TIP]
        index = hand[self.INDEX_TIP]

        return self.distance(
            thumb,
            index
        ) < 35

    # ------------------------------------
    # Spell Recognition
    # ------------------------------------

    def detect_spell(self, hand):

        thumb, index, middle, ring, pinky = self.finger_states(hand)

        # MAGIC
        if self.is_pinching(hand):
            return "MAGIC"

        # SHIELD
        if index and middle and ring and pinky:
            return "SHIELD"

        # FIREBALL
        if index and middle and not ring and not pinky:
            return "FIREBALL"

        # LASER
        if index and not middle and not ring and not pinky:
            return "LASER"

        return "NONE"

    # ------------------------------------
    # Palm Position
    # ------------------------------------

    def get_palm(self, hand):

        return hand[9]