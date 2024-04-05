import pygame as pg
import sprites


class Koopa:
    def __init__ (self, x, y):
        self.koopa_x = x 
        self.koopa_y = y
        self.sprite_index=0 
        self.sprite = sprites.KOOPA  # Initial sprite KOOPA
        self.koopa_width = 48  
        self.koopa_height = 48  
        self.rect = pg.Rect(self.koopa_x,self.koopa_y, self.koopa_width, self.koopa_height)
        self.koopa_velocity_x = -0.05
    
    def update(self):
        self.koopa_x += self.koopa_velocity_x
        self.sprite_index = (self.sprite_index + 1) % len(sprites.KOOPA)
        self.koopa_velocity_x = -0.05

    def move_right(self):
        self.koopa_velocity_x = 0.1  # Set horizontal velocity for moving right

    def draw(self, screen):
        screen.blit(sprites.tile_set, (self.koopa_x, self.koopa_y), sprites.KOOPA[self.sprite_index])