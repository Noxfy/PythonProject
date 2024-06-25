import pygame, util

player_sprites = pygame.image.load("./assets/player_sprite.png")

def RenderPlayer(screen, player_position):

  direction = 0

  angle = util.GetLookDirection(player_position)
  if (angle > -4 and angle < -2):
    direction = 0
  elif (angle < 0.5 and angle > -1):
    direction = 1
  elif (angle < -1 and angle > -2):
    direction = 3
  else:
    direction = 2

  screen.blit(player_sprites.subsurface(13 * direction, 0, 13, 17), player_position)
