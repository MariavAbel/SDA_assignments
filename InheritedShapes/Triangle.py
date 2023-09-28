from abc import ABC
from abc import ABCMeta, abstractmethod
import pygame
from pygame.locals import *
import pygwidgets
import sys
import random
from Shape import *

class Triangle(Shape):
    def __init__(self, window, maxWidth, maxHeight):
        super().__init__(window, 'Triangle', maxWidth, maxHeight)

    def clickedInside(self, mousePoint):
        mouse_x, mouse_y = mousePoint
        x, y = mouse_x - self.left, mouse_y - self.top
        #when the mousePoint is not in the rect
        if not (0 <= x <= self.width and 0 <= y <= self.height):
            return False
        #do some math to see if the point is inside the triangle
        if self.triangleSlope >= 0:
            return y >= self.triangleSlope * x
        else:
            return y <= self.triangleSlope * x + self.height
        
    def getArea(self):
        return 0.5 * self.width * self.height
        
    def draw(self):
        pygame.draw.polygon(self.window, self.color, [(self.left, self.top + self.height),(self.left + self.width, self.top + self.height),(self.left + self.width / 2, self.top)])
         