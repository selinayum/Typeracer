import pygame
import sys
from pygame.locals import *

# width and height
# Text color
# bg color


class Constants:
    WIDTH = 750
    HEIGHT = 500
    TEXT_COLOR = (255, 232, 123)
    BG_COLOR = (66, 66, 66)


WINDOW = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
pygame.display.set_caption('Typeracer >:)')

pygame.init()

while True:
    pygame.display.update()
#selina