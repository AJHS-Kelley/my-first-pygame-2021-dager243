# My First PyGame, Beau Diaz-Perez, 11/29/2021 2:52pm v0.4

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

# Fill background color
windowSurface.fill(WHITE)

#draw a polygon onto the screen.
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106))