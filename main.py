import pygame as pg
from pygame.locals import *
import menu
import sprites
from player import Player


pg.init()

screen_width, screen_height = 744, 672
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Super Mario Bros 1-1")

player = Player(100,552)

background = sprites.background.convert()

show_menu = True
while show_menu:
    show_menu = menu.display_menu(screen)
    

# Game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.move_left()
            elif event.key == K_RIGHT:
                player.move_right()
            elif event.key == K_UP:
                player.jump()
        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                player.stop_x_movement()

    screen.blit(background, (0,0))
    player.update()
    player.check_collision()
    player.draw(screen)
    pg.display.flip()

pg.quit()
