import pygame, sys, renderer
from enum import Enum

#from util import normalize


class PlayerDirection(Enum):
  North = 0
  South = 1
  West = 2
  East = 3


player_state = PlayerDirection.North
player_moving = False
player_position = [0, 0]
player_speed = 0.1
player_move_vec = [0, 0]


def HandelEvents():
  global player_move_vec
  global player_state
  global player_moving
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_w:
        player_move_vec[1] += 1
        player_state = PlayerDirection.North
        player_moving = True
      if event.key == pygame.K_d:
        player_move_vec[0] += 1
        player_state = PlayerDirection.East
        player_moving = True
      if event.key == pygame.K_s:
        player_move_vec[1] -= 1
        player_state = PlayerDirection.South
        player_moving = True
      if event.key == pygame.K_a:
        player_move_vec[0] -= 1
        player_state = PlayerDirection.West
        player_moving = True
      #direction = normalize(direction)

    if event.type == pygame.KEYUP and (event.key == pygame.K_w or event.key
                                       == pygame.K_a or event.key == pygame.K_s
                                       or event.key == pygame.K_d):
      player_moving = False
      player_move_vec = [0, 0]
  if (player_moving):
    player_position[0] += player_move_vec[0] * player_speed
    player_position[1] -= player_move_vec[1] * player_speed
    print("moving")


def Render(screen):
  screen.fill((255, 255, 255))

  renderer.RenderPlayer(screen, player_state, player_position)

  pygame.display.update()
