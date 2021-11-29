# My First PyGame, Beau Diaz-Perez, 11/29/2021 2:42pm v0.3

import pygame, sys
from pygame.locals import *

#start pygame
pygame.init()

#setup our window.
windowSurface = pygame.display.set_mode((500,400), 0, 32)
pygame.display.set_caption('hello, world!')

#setup colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# setup font.
basicfont = pygame.font.sysfont(None, 48)

# setup text.
text = basicFont.render('hello, world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery