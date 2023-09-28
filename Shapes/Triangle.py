import pygame
from pygame.locals import *
import sys
import random

RED = (255, 0, 0)
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255)

class Triangle():
    #3 initializing the triangle object
    def __init__(self, window, maxWidth, maxHeight):
        self.window = window
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.width = random.randint(10, 100)
        self.height = random.randint(10, 100)
        self.triangleSlope = -1 * (self.height / self.width)
        self.left = random.randint(1, maxWidth - self.width - 1)
        self.top = random.randint(25, maxHeight - self.height - 1)
        self.shapeType = 'Triangle'

    #4 defining a method to check if the location clicked is inside that triangle
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

#5 defining a method, which returns the information that the itme clicked is a triangle
    def getType(self):
        return self.shapeType
    
#6 defining a method, which calculates the area of the triangle
    def getArea(self):
        return 0.5 * self.width * self.height
#7 defining a method, to draw the triangle in a randomly chosen color
    def draw(self):
        pygame.draw.polygon(self.window, self.color, [(self.left, self.top + self.height),(self.left + self.width, self.top + self.height),(self.left + self.width / 2, self.top)])
                                                      
                                                      