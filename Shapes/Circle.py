import pygame
from pygame.locals import *
import sys
import random

RED = (255, 0, 0)
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255)

class Circle():

    #3 initializing circle object
    def __init__(self, window, maxWidth, maxHeight):
        self.window = window
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.radius = random.randint(10, 50)
        self.x = random.randint(1, maxWidth - 100)
        self.y = random.randint(25, maxHeight - 100)
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        self.shapeType = 'Circle'

    #4 defining a method to check if the location clicked is inside that circle
    def clickedInside(self, mousePoint):
        mouse_x, mouse_y = mousePoint
        distance = ((mouse_x - (self.x + self.radius))**2 + (mouse_y - (self.y + self.radius))**2)**0.5
        return distance <= self.radius

    #5 defining a method, which returns the information that the itme clicked is a circle
    def getType(self):
        return self.shapeType

    #6 defining a method, which calculates the area of the circle
    def getArea(self):
        return 3.14 * (self.radius**2)

    #7 defining a method, to draw the circle in a randomly chosen color
    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.x + self.radius, self.y + self.radius), self.radius)