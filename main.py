import pygame as pg
from pygame.locals import *
from menu

pg.init()

screen_width, screen_height = 744, 672
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Super Mario Bros 1-1")

menu.display_menu(screen)

# Game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
    screen.fill((0, 0, 0))
    pg.display.flip()

pg.quit()
