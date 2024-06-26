import pygame

import backEnd, variables

pygame.init()
screen = pygame.display.set_mode((variables.width, variables.height))
pygame.display.set_caption('Hello World!')
while True:
   backEnd.HandelEvents()
   backEnd.Update()
   backEnd.Render(screen)