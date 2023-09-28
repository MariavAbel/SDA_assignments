from abc import ABC
from abc import ABCMeta, abstractmethod
import pygame
from pygame.locals import *
import pygwidgets
import sys
import random


RED = (255, 0, 0)
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255)

class Shape():
    def __init__(self, window, shapeType, maxWidth, maxHeight):
        self.window = window
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.radius = random.randint(10, 50)
        self.x = random.randint(1, maxWidth - 100)
        self.y = random.randint(25, maxHeight - 100)
        self.width = random.randint(10, 100)
        self.height = random.randint(10, 100)
        self.left = random.randint(1, maxWidth - self.width - 1)
        self.top = random.randint(25, maxHeight - self.height - 1)
        self.triangleSlope = -1 * (self.height / self.width)
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
        self.shapeType = shapeType

    @abstractmethod
    def clickedInside(self, mousePoint):
        raise NotImplementedError

#5 defining a method, which returns the information that the itme clicked is a triangle
    def getType(self):
        return self.shapeType
    
    @abstractmethod
    def getArea(self, mousepoint):
        raise NotImplementedError

    @abstractmethod
    def draw(self):
        raise NotImplementedError
