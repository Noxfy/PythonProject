import pygame, sys, renderer
from enum import Enum

import util

class PlayerDirection(Enum):
  North = 0
  South = 1
  West = 2
  East = 3

player_state = PlayerDirection.North
player_moving = False
player_position = [0, 0]
player_speed = 0.01
player_move_vec = [0, 0]
  
def HandelEvents():
  global player_move_vec
  global player_moving
  for event in pygame.event.get():
    
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    HandleMovement(event)

  if (player_moving):
    #move player
    player_position[0] += player_move_vec[0] * player_speed
    player_position[1] -= player_move_vec[1] * player_speed


def Render(screen):
  screen.fill((255, 255, 255))

  renderer.RenderPlayer(screen, player_position)
  
  print(util.GetLookDirection(player_position))

  pygame.display.update()


def HandleMovement(event):
  global player_state
  global player_moving
  global player_move_vec
  keys = pygame.key.get_pressed()
  if event.type == pygame.KEYDOWN:
    if keys[pygame.K_w]:
      player_move_vec[1] += 1
      player_state = PlayerDirection.North
      player_moving = True
    if keys[pygame.K_d]:
      player_move_vec[0] += 1
      player_state = PlayerDirection.East
      player_moving = True
    if keys[pygame.K_s]:
      player_move_vec[1] -= 1
      player_state = PlayerDirection.South
      player_moving = True
    if keys[pygame.K_a]:
      player_move_vec[0] -= 1
      player_state = PlayerDirection.West
      player_moving = True
    player_move_vec = util.normalize_vector(player_move_vec)
    
  if event.type == pygame.KEYUP and not (keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]):
    player_moving = False
    player_move_vec = [0, 0]