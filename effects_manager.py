import random


class EffectsManager:

    def __init__(self, particles):

        self.particles = particles

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self):

        self.particles.update()

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(self, frame):

        self.particles.draw(frame)

    # ---------------------------------
    # Aura Effect
    # ---------------------------------

    def aura(self, x, y):

        self.particles.emit(
            x,
            y,
            count=3
        )

    # ---------------------------------
    # Burst Effect
    # ---------------------------------

    def burst(self, x, y):

        self.particles.emit(
            x,
            y,
            count=10
        )

    # ---------------------------------
    # Explosion Effect
    # ---------------------------------

    def explosion(self, x, y):

        self.particles.emit(
            x,
            y,
            count=18
        )

    # ---------------------------------
    # Portal Effect
    # ---------------------------------

    def portal(self, x, y):

        self.particles.emit(
            x,
            y,
            count=12
        )

    # ---------------------------------
    # Lightning Sparks
    # ---------------------------------

    def lightning(self, x, y):

        self.particles.emit(
            x,
            y,
            count=6
        )

    # ---------------------------------
    # Magic Rain
    # ---------------------------------

    def magic_rain(self, x, y):

        for _ in range(5):

            self.particles.emit(
                x + random.randint(-60, 60),
                y + random.randint(-60, 60),
                count=2
            )

    # ---------------------------------
    # Clear All
    # ---------------------------------

    def clear(self):

        self.particles.clear()