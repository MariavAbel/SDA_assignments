from abc import ABC
from abc import ABCMeta, abstractmethod
import pygame
from pygame.locals import *
import pygwidgets
import sys
import random
from Shape import *

class Circle(Shape):
    def __init__(self, window, maxWidth, maxHeight):
        super().__init__(window, 'Circle', maxWidth, maxHeight)

    def clickedInside(self, mousePoint):
        mouse_x, mouse_y = mousePoint
        distance = ((mouse_x - (self.x + self.radius))**2 + (mouse_y - (self.y + self.radius))**2)**0.5
        return distance <= self.radius
    
    #6 defining a method, which calculates the area of the circle
    def getArea(self):
        return 3.14 * (self.radius**2)
    
    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.x + self.radius, self.y + self.radius), self.radius)