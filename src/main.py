import pygame, math

import backEnd, variables, roomManager

pygame.init()
screen = pygame.display.set_mode((variables.width, variables.height))
pygame.display.set_caption('Hello World!')
roomManager.generateRoom(math.floor(variables.width / variables.terrain_scale), math.floor(variables.height / variables.terrain_scale))
while True:
   backEnd.HandelEvents()
   backEnd.Update()
   backEnd.Render(screen)