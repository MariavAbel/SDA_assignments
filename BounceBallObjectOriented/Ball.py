import pygame
from pygame.locals import *
import random

class Ball():
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.image = pygame.image.load('images/Ball.png')

        #2
        self.ballRect = self.image.get_rect()

        self.maxWidth = windowWidth
        self.minWidth = 0
        self.maxHeight = windowHeight
        self.minHeight = 0

        # self.x = windowWidth/2
        # self.y = windowHeight/2
        self.ballRect.x = (windowWidth - self.image.get_width())/2
        self.ballRect.y = (windowHeight - self.image.get_height())/2

        #3
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)

        #4
        speedsList = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.xspeed = random.choice(speedsList)
        self.yspeed = random.choice(speedsList)

    #5
    def update(self):

        #check for hitting a wall. if so, change that direction
        if self.ballRect.left <= 0 or self.ballRect.right >= self.maxWidth:
            self.xspeed = -self.xspeed

        if self.ballRect.top <= 0 or self.ballRect.bottom >= self.maxHeight:
            self.yspeed = -self.yspeed

        #update the ball's x and y, using the speed in two directions
        self.ballRect.move_ip(self.xspeed, self.yspeed)

    def draw(self):
        self.window.blit(self.image, self.ballRect)