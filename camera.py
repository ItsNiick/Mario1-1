import pygame as pg
from pygame.locals import *
import sprites
import player

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity[0] + self.camera.topleft[0], entity[1] + self.camera.topleft[1]

    def update(self, player_position):
        x = -player_position[0] + int(744 / 2)
        y = -player_position[1] + int(672 / 2)

        # Limit scrolling to the boundaries of the level
        x = min(0, x)  # Left boundary
        y = min(0, y)  # Top boundary
        x = max(-(self.width - 744), x)  # Right boundary
        y = max(-(self.height - 672), y)  # Bottom boundary
        self.camera = pg.Rect(x, y, self.width, self.height)
