import sys
import pygame
from pygame.locals import *

white1 = 255,255,255

blue = 0,0,200

pygame.init()

screen = pygame.display.set_mode((600,500))

my_font = pygame.font.Font(None,60)

text_image = my_font.render('Hello Pygame',True,white1)

while True:

    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill(blue)
    screen.blit(text_image,(100,100))
    pygame.display.update()

