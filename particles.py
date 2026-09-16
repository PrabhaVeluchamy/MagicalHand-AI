import cv2
import random


class Particle:

    def __init__(self, x, y):

        self.x = float(x)
        self.y = float(y)

        self.dx = random.uniform(-2.5, 2.5)
        self.dy = random.uniform(-3.5, -1.0)

        self.life = 30
        self.max_life = 30

        self.radius = random.randint(2, 4)

        self.color = random.choice([
            (0, 140, 255),
            (0, 180, 255),
            (0, 220, 255),
            (0, 255, 255),
            (255, 255, 255)
        ])

    def update(self):

        self.x += self.dx
        self.y += self.dy

        # Gravity
        self.dy += 0.08

        # Air resistance
        self.dx *= 0.99

        self.life -= 1

    def draw(self, frame):

        if self.life <= 0:
            return

        alpha = self.life / self.max_life

        color = (
            int(self.color[0] * alpha),
            int(self.color[1] * alpha),
            int(self.color[2] * alpha)
        )

        cv2.circle(
            frame,
            (int(self.x), int(self.y)),
            self.radius,
            color,
            -1,
            cv2.LINE_AA
        )


class ParticleSystem:

    def __init__(self):

        self.particles = []

        # Prevent unlimited particle growth
        self.MAX_PARTICLES = 300

    # ---------------------------------

    def emit(self, x, y, count=5):

        if len(self.particles) >= self.MAX_PARTICLES:
            return

        count = min(
            count,
            self.MAX_PARTICLES - len(self.particles)
        )

        for _ in range(count):
            self.particles.append(
                Particle(x, y)
            )

    # ---------------------------------

    def update(self):

        alive = []

        for p in self.particles:

            p.update()

            if p.life > 0:
                alive.append(p)

        self.particles = alive

    # ---------------------------------

    def draw(self, frame):

        for p in self.particles:
            p.draw(frame)

    # ---------------------------------

    def clear(self):

        self.particles.clear()

    # ---------------------------------

    def count(self):

        return len(self.particles)