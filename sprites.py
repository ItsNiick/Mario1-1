from os import path
import pygame as pg
from PIL import Image

images_folder = path.join(path.dirname(__file__), 'images')

tile_set = pg.image.load(path.join(images_folder, 'tile_set.png'))
tile_set_flipped = pg.image.load(path.join(images_folder, 'tile_set_flipped.png'))
text_image = pg.image.load(path.join(images_folder, 'text_image.png'))
background = pg.image.load(path.join(images_folder, 'background.png'))
background2 = pg.image.load(path.join(images_folder, 'background2.png'))
foreground = pg.image.load(path.join(images_folder, 'foreground.png'))
menu = pg.image.load(path.join(images_folder, 'menu.png'))
digits = pg.image.load(path.join(images_folder, 'digits.png'))
level_1_1 = Image.open(path.join(images_folder, 'map.png'))

#Sprite rectangles to retrieve section of sprite sheet
EMPTY_SPRITE = (240, 48, 48, 48)

SMALL_MARIO_MOVE = [
    (0, 168, 48, 48),
    (48, 168, 48, 48),
    (96, 168, 48, 48)
]

SMALL_MARIO_IDLE = (294, 168, 36, 48)
SMALL_MARIO_JUMP = (192, 168, 48, 48)
SMALL_MARIO_BRAKE = (150, 168, 40, 48)
DEAD_MARIO = (243, 168, 42, 42)
SMALL_MARIO_FLAGPOLE = [
    (342, 168, 39, 48),
    (380, 168, 39, 48)
]

MIDDLE_MARIO_IDLE = (48, 327, 48, 72)

BIG_MARIO_IDLE = (289, 216, 48, 96)
BIG_MARIO_RUN = [
    (0, 216, 48, 96),
    (48, 216, 48, 96),
    (96, 216, 48, 96)
]
BIG_MARIO_JUMP = (192, 216, 48, 96)
BIG_MARIO_BRAKE = (144, 216, 48, 96)
MARIO_CROUCH = (240, 246, 48, 66)
MARIO_SWIM = (0, 311, 48, 88)

GROW_SPRITES = [
    SMALL_MARIO_IDLE,
    MIDDLE_MARIO_IDLE,
    BIG_MARIO_IDLE
]

SHRINK_SPRITES = [
    MARIO_SWIM,
    EMPTY_SPRITE,
    SMALL_MARIO_IDLE
]

KOOPA = [
    (0, 96, 48, 72),
    (48, 96, 48, 72)
]

KOOPA_SHELL = (96, 126, 48, 42)

GOOMBA_RUN = [
    (0, 48, 48, 48),
    (48, 48, 48, 48)
]
GOOMBA_SQUISHED = (96, 48, 48, 48)
GOOMBA_KNOCKED = (144, 48, 48, 48)

BRICK = (0, 0, 48, 48)
BRICK_FRAGMENT = [
    (252, 12, 24, 24),
    (300, 12, 24, 24)
]

Q_BLOCK_OPEN = (48, 0, 48, 48)
Q_BLOCK_CLOSED = [
    (96, 0, 48, 48),
    (144, 0, 48, 48),
    (192, 0, 48, 48)
]

COIN = [
    (144, 126, 48, 42),
    (192, 126, 48, 42),
    (240, 126, 48, 42),
    (288, 126, 48, 42)
]

FLAG = (336, 0, 48, 48)

WIN_SPRITES_BIG = [
    (339, 216, 48, 96),
    (387, 216, 48, 96)
]

WIN_SPRITES_SMALL = [
    (339, 168, 42, 48),
    (390, 168, 42, 48)
]

SELECTOR = (394, 12, 24, 24)