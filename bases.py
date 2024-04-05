from typing import Any
import pygame as pg
import math


class Object():
    def __init__(self, rect):
        self.rect = rect

    def __getattr__(self, name):
        return getattr(self.rect, name)
    
    def __setattr__(self, name, value):
        if name == 'pos':
            self.rect.pos = value
        else:
            object.__setattr__(self, name, value)

class Vector2D():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return Vector2D(self.x * other, self.y * other)
    
    def __add__(self,other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
class Rectangle():
    def __init__(self, pos = Vector2D(), w = 0, h = 0):
        self.pos = pos
        self.w = w
        self.h = h

    def overlap(self, other):
        return not(other.pos.x + other.w <= self.pos.x or
                   other.pos.x >= self.pos.x + self.w or
                   other.pos.y + other.h <= self.pos.y or
                   other.pos.y >= self.pos.y + self.h)

    def check_collision(self, collider_list):
        for collider in collider_list:
            if abs(self.pos.x - collider.pos.x) < 100 or collider.rect.w >= 100:
                if self.overlap(collider):
                    return collider
                
    