import pygame
from constant import *

class Widget:
    def __init__(self, rect):
        if not isinstance(rect, pygame.Rect):
            rect = pygame.Rect(rect)
        self.rect = rect
        self.callback = {}
 
    def is_over(self, point):
        point_x, point_y = point
        x, y = self.rect.x, self.rect.y

        in_x = point_x > x and point_x < x + self.rect.width
        in_y = point_y > y and point_y < y + self.rect.height
        return in_x and in_y

    def connect(self,event,function):
        self.callback[event] = function

    def render(self, surface):
        pygame.draw.rect(surface, gray,self.rect)