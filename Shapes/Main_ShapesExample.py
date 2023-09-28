import pygame
from pygame.locals import *
import sys
import random
import pygwidgets
from Circle import *
from Triangle import *

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_SHAPES = 10

def main():
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    shapesList = []
    shapeClassesTuple = (Circle, Triangle)
    for _ in range(N_SHAPES):
        randomlyChosenClass = random.choice(shapeClassesTuple)
        oShape = randomlyChosenClass(window, WINDOW_WIDTH, WINDOW_HEIGHT)
        shapesList.append(oShape)
    oStatusLine = pygwidgets.DisplayText(window, (50, 50), "Click on shapes")
    while True:
        #check for and handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                 #REVERSE ORDER TO CHECK LAST DRAWN shape first
                 for oShape in reversed(shapesList):
                      if oShape.clickedInside(event.pos):
                           theType = oShape.getType()
                           area = oShape.getArea()
                           newText = 'Clicked on a ' + theType + ' whose are is ' + str(area)
                           oStatusLine.setValue(newText)
                           break
        window.fill((255, 255, 255))
        for oShape in shapesList:
            oShape.draw()

        oStatusLine.draw()
        pygame.display.update()
        clock.tick(FRAMES_PER_SECOND)
if __name__ == "__main__":
    main()