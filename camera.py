import pygame as pg
from pygame.locals import *


class Camera:
    def setup(self, width, height):
        self.width = width
        self.height = height
        self.x = 0 
        self.y = 0

    def follow(self, target):
        self.x = target.x - self.width / 2
        self.y = target.y - self.height / 2
        
        self.x = max(0, min(self.x, 10176 - self.width))
        self.y = max(0, min(self.y, 10176 - self.height))

    def apply(self, entity):
        return entity.x - self.x, entity.y - self.y