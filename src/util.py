import math, pygame
from enum import Enum
from perlin_noise import PerlinNoise

import variables, roomManager

class PlayerDirection(Enum):
  North = 0
  South = 1
  West = 2
  East = 3

def GetLookDirection(player_pos):
    mouse_pos = pygame.mouse.get_pos()

    vec2 = [None, None]
    vec2[0] = mouse_pos[0] - player_pos.x
    vec2[1] = mouse_pos[1] - player_pos.y
    vec1 = [0, 1]

    angle_to_mouse = math.atan2(vec2[1], vec2[0]) - math.atan2(vec1[1], vec1[0])

    return angle_to_mouse


def OutOfBounds(position):
    return position[0] < 0 or position[0] > variables.width or position[1] < 0 or position[1] > variables.height

def getPerlinNoise(oct):
  noise = PerlinNoise(oct, None)
  xpix, ypix = 100, 100
  pic = []
  for i in range(xpix):
      row = []
      for j in range(ypix):
          noise_val = noise([i/xpix, j/ypix]) * 10
          row.append(noise_val)
      pic.append(row)
  return pic

def isCollidingWithTerrain(collider_rect):
    for rect in roomManager.rects:
        if pygame.Rect.colliderect(rect[0], collider_rect):
            return rect
    return None