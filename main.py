import pygame as pg
from pygame.locals import *
import menu
import sprites
from player import Player

SCREEN_WIDTH, SCREEN_HEIGHT = 744, 672

pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Super Mario Bros 1-1")

player = Player(100,552)
camera_x = 0
camera_y = 0

background = sprites.background.convert()
background_x = 0

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

    player_position = player.update()
    camera_x = max(0, min(player.x - SCREEN_WIDTH // 2, background.get_width() - SCREEN_WIDTH))
    camera_y = max(0, min(camera_y, 672 - SCREEN_HEIGHT))
    scroll_speed = int(player.velocity_x * 2)
    #background_x -= scroll_speed
    #background_x = max(0, min(background_x, background.get_width() - SCREEN_WIDTH))

    if player.velocity_x > 0:
        background_x -= abs(player.velocity_x)
    #elif player.velocity_x < 0:
        #background_x += abs(player.velocity_x)
    background_x = max(0, background_x)

    #if player.velocity_x != 0:
        #velocity_int = int(player.velocity_x)
        #background.scroll(-velocity_int, 0)
    if background_x < 0:
        background_x = 0
    elif background_x > background.get_width() - SCREEN_WIDTH:
        #background_x = background.get_width() - SCREEN_WIDTH
        pass

    #screen.blit(background, (-background_x,0), (camera_x, camera_y, SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(background, (-camera_x,0))

    player.check_collision()
    player.draw(screen, camera_x, camera_y)
    pg.display.flip()

pg.quit()
