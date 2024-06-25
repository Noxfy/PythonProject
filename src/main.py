import pygame

import backEnd

pygame.init()
screen = pygame.display.set_mode((256, 256))
pygame.display.set_caption('Hello World!')
while True:
   backEnd.HandelEvents()
   backEnd.Update()
   backEnd.Render(screen)