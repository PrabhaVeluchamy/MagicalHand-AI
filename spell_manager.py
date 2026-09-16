import cv2


class SpellManager:

    def __init__(self,
                 renderer,
                 particles,
                 beam,
                 portal,
                 effects,
                 magic_image):

        self.renderer = renderer
        self.particles = particles
        self.beam = beam
        self.portal = portal
        self.effects = effects
        self.magic = magic_image

    # ---------------------------------
    # MAGIC
    # ---------------------------------

    def magic_spell(self, frame, palm):

        self.renderer.draw_magic_circle(
            frame,
            self.magic,
            palm,
            170
        )

        self.effects.aura(
            palm[0],
            palm[1]
        )

    # ---------------------------------
    # SHIELD
    # ---------------------------------

    def shield_spell(self, frame, palm):

        self.portal.draw(
            frame,
            palm,
            110
        )

        self.effects.burst(
            palm[0],
            palm[1]
        )

    # ---------------------------------
    # FIREBALL
    # ---------------------------------

    def fireball_spell(self, frame, palm):

        cv2.circle(
            frame,
            palm,
            35,
            (0, 140, 255),
            -1,
            cv2.LINE_AA
        )

        self.effects.explosion(
            palm[0],
            palm[1]
        )

    # ---------------------------------
    # LASER
    # ---------------------------------

    def laser_spell(self, frame, palm):

        end = (frame.shape[1], palm[1])

        self.beam.draw(
            frame,
            palm,
            end
        )

    # ---------------------------------
    # PORTAL
    # ---------------------------------

    def portal_spell(self,
                     frame,
                     palm1,
                     palm2):

        self.renderer.draw_magic_circle(
            frame,
            self.magic,
            palm1,
            150
        )

        self.renderer.draw_magic_circle(
            frame,
            self.magic,
            palm2,
            150
        )

        self.beam.draw(
            frame,
            palm1,
            palm2
        )

        center = (
            (palm1[0] + palm2[0]) // 2,
            (palm1[1] + palm2[1]) // 2
        )

        self.portal.draw(
            frame,
            center,
            140
        )

        self.effects.burst(
            center[0],
            center[1]
        )