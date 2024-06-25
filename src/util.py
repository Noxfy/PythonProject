import math, pygame
from enum import Enum

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

    #angle_to_mouse = math.atan((mouse_pos[0] - player_pos[0]) / (mouse_pos[1] - player_pos[1])) * (180/math.pi)
    angle_to_mouse = math.atan2(vec2[1], vec2[0]) - math.atan2(vec1[1], vec1[0])

    return angle_to_mouse