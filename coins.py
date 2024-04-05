import pygame as pg
import sprites
from player import Player

class Coin:
    def __init__(self, x, y):
        self.coin_x = x
        self.coin_y = y
        self.sprite_index = 0
        self.sprite = sprites.COIN
        self.coin_width = 48
        self.coin_height = 48
        self.rect = pg.Rect(self.coin_x, self.coin_y, self.coin_width, self.coin_height)
        self.coin_velocity_x = -0.05

    def update(self):
        self.coin_x += self.coin_velocity_x
        self.sprite_index = (self.sprite_index + 1) % len(sprites.KOOPA)
        self.coin_velocity_x = -0.05

    def draw(self, screen):
        screen.blit(sprites.tile_set, (self.coin_x, self.coin_y), sprites.COIN[self.sprite_index])
    
    #def collision(self):
        #if self.rect.colliderect():
            #coin_sound = pg.mixer.Sound('sounds/coin.ogg')
            #coin_sound.play()