import pygame as pg
from pygame.locals import *
#import sprites

class Timer:
    def __init__(self):
        self.start_timer = 0
        self.elapsed_timer = 0
        self.run = False
    def start(self):
        self.start_timer = pg.time.get_ticks()
        self.run = True
    def stop(self):
        self.elapsed_timer = 0
        self.run = False
    def reset(self):
        self.elapsed_timer = 0 
        if self.run:
            self.start_timer = pg.time.get_ticks()
    def update(self):
        if self.run:
            current_time = pg.time.get_ticks()
            self.elapsed_timer = current_time - self.start_timer
    def get_elapsed_time(self):
        return self.elapsed_timer

    def get_elapsed_time_seconds(self):
        return self.elapsed_timer / 1000
