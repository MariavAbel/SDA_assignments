import pygame
from pygame.locals import *
import sys
import random
from Ball import *

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

def main():
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
   
    oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    oBall.minWidth = 0
    oBall.minHeight = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        oBall.update()
        window.fill(BLACK)
        oBall.draw()
        pygame.display.update()

        clock.tick(FRAMES_PER_SECOND)
            

if(__name__ == '__main__'):
    main()
