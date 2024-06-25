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
player_position = pygame.Vector2(0, 0)
player_speed = 0.01 
player_move_vec = pygame.Vector2(0, 0)

max_speed = 0.1
acceleration = 0.1
deceleration = 0.1
velocity = pygame.Vector2(0, 0)
  
def HandelEvents():
  global player_move_vec
  global player_moving
  global player_position
  for event in pygame.event.get():
    
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    HandleMovement(event)

  if (player_moving):
    #move player
    player_position += velocity

def Render(screen):
  screen.fill((255, 255, 255))

  renderer.RenderGround(screen)
  renderer.RenderPlayer(screen, player_position)

  pygame.display.update()


def HandleMovement(event):
  global player_state
  global player_moving
  global player_move_vec
  global velocity
  keys = pygame.key.get_pressed()
  if event.type == pygame.KEYDOWN:
    player_move_vec = pygame.Vector2(0, 0)
    velocity = player_move_vec

    if keys[pygame.K_w]:
      player_move_vec.y -= 1
      player_moving = True
    if keys[pygame.K_d]:
      player_move_vec.x += 1
      player_moving = True
    if keys[pygame.K_s]:
      player_move_vec.y += 1
      player_moving = True
    if keys[pygame.K_a]:
      player_move_vec.x -= 1
      player_moving = True
    #normalize vector
    if player_move_vec.length() > 0:
      player_move_vec = player_move_vec.normalize()

    #apply acceleration or deceleration
    if player_move_vec.length() > 0:
        velocity += player_move_vec * acceleration
        if velocity.length() > max_speed:
            velocity = velocity.normalize() * max_speed
    else:
        if velocity.length() > 0:
            velocity -= velocity.normalize() * deceleration
            if velocity.length() < deceleration:
                velocity = pygame.Vector2(0, 0)
    
  if event.type == pygame.KEYUP and not (keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]):
    player_moving = False