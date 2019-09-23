import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A ckass to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """ Create a bullet object at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen # On page 258
