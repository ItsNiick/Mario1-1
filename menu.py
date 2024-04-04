import pygame as pg
from pygame.locals import *
import sprites


def display_menu(screen):
    #Loads main menu
    menu_image = pg.image.load('images/menu.png')
    selected_option = 0
    selector_y = 402

    #Main Menu loop
    show_menu = True
    while show_menu:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    show_menu = False
                elif event.key == K_UP:
                    selected_option = (selected_option - 1) % 2
                elif event.key == K_DOWN:
                    selected_option = (selected_option + 1) % 2

        screen.blit(menu_image, (0, 0))

        selector_x = 250  # X-coordinate of the selector
        screen.blit(sprites.tile_set, (selector_x, selector_y + selected_option * 46), sprites.SELECTOR) # Draws and moves the selector up or down 46 pixels when up/down pressed

        pg.display.flip()