import math, pygame, variables
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
    for x in range(len(roomManager.current_room)):
        for y in range(len(roomManager.current_room[x])):
            tile = roomManager.current_room[x][y]
            if tile != None and tile.has_collision and pygame.Rect.colliderect(pygame.rect.Rect(tile.tile_position.x * variables.terrain_scale, tile.tile_position.y * variables.terrain_scale, variables.terrain_scale, variables.terrain_scale), collider_rect):
                return tile
    return None