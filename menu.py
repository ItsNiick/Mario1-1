import pygame as pg
from pygame.locals import *

def display_menu(screen):
    #Loads main menu
    menu_image = pg.image.load('images/menu.png')

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
        screen.blit(menu_image, (0, 0))
        pg.display.flip()