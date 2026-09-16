import cv2
import time

from gesture import GestureDetector
from renderer import Renderer
from particles import ParticleSystem
from beam import EnergyBeam
from portal import Portal
from hud import HUD

from effects_manager import EffectsManager
from spell_manager import SpellManager


class MagicGame:

    def __init__(self):

        # -----------------------------
        # Core Modules
        # -----------------------------
        self.gesture = GestureDetector()

        self.renderer = Renderer()

        self.particles = ParticleSystem()

        self.beam = EnergyBeam()

        self.portal = Portal()

        self.hud = HUD()

        self.effects = EffectsManager(
            self.particles
        )

        # -----------------------------
        # Load Assets
        # -----------------------------
        self.magic = cv2.imread(
            "assets/magic_circle.png",
            cv2.IMREAD_UNCHANGED
        )

        if self.magic is None:
            raise FileNotFoundError(
                "assets/magic_circle.png not found."
            )

        # -----------------------------
        # Spell Manager
        # -----------------------------
        self.spells = SpellManager(
            self.renderer,
            self.particles,
            self.beam,
            self.portal,
            self.effects,
            self.magic
        )

        # -----------------------------
        # Game Variables
        # -----------------------------
        self.current_spell = "NONE"

        self.last_cast = 0

        self.cooldown = 0.15

        self.frame_count = 0

        self.show_hud = True

        self.recording = False
    def update(self, frame, hands):

        self.frame_count += 1

        now = time.time()

        # -----------------------------
        # Update Effects
        # -----------------------------
        if self.frame_count % 2 == 0:
            self.effects.update()

        self.current_spell = "NONE"

        # ===================================================
        # ONE HAND MODE
        # ===================================================

        if len(hands) == 1:

            hand = hands[0]

            palm = self.gesture.get_palm(hand)

            spell = self.gesture.detect_spell(hand)

            if now - self.last_cast >= self.cooldown:

                self.current_spell = spell

                if spell == "MAGIC":

                    self.spells.magic_spell(
                        frame,
                        palm
                    )

                elif spell == "SHIELD":

                    self.spells.shield_spell(
                        frame,
                        palm
                    )

                elif spell == "FIREBALL":

                    self.spells.fireball_spell(
                        frame,
                        palm
                    )

                elif spell == "LASER":

                    self.spells.laser_spell(
                        frame,
                        palm
                    )

                self.last_cast = now

        # ===================================================
        # TWO HAND MODE
        # ===================================================

        elif len(hands) >= 2:

            hand1 = hands[0]
            hand2 = hands[1]

            palm1 = self.gesture.get_palm(hand1)
            palm2 = self.gesture.get_palm(hand2)

            self.current_spell = "PORTAL"

            self.spells.portal_spell(
                frame,
                palm1,
                palm2
            )

        # ===================================================
        # DRAW EFFECTS
        # ===================================================

        self.effects.draw(frame)

        # ===================================================
        # HUD
        # ===================================================

        if self.show_hud:

            self.hud.draw(
                frame,
                self.current_spell,
                len(hands)
            )
    # ===================================================
    # KEYBOARD CONTROLS
    # ===================================================

    def handle_key(self, key):

        # Toggle HUD
        if key == ord("h"):
            self.show_hud = not self.show_hud

        # Clear all particles
        elif key == ord("c"):
            self.effects.clear()

        # Toggle Recording (Future Feature)
        elif key == ord("r"):
            self.recording = not self.recording

            if self.recording:
                print("Recording Started")
            else:
                print("Recording Stopped")

        # Screenshot (Future Feature)
        elif key == ord("s"):
            print("Screenshot feature coming soon...")

    # ===================================================
    # RESET GAME
    # ===================================================

    def reset(self):

        self.effects.clear()

        self.current_spell = "NONE"

        self.last_cast = 0

        self.frame_count = 0

    # ===================================================
    # GET CURRENT SPELL
    # ===================================================

    def get_spell(self):

        return self.current_spell

    # ===================================================
    # CLEANUP
    # ===================================================

    def close(self):

        self.reset()