import pygame, util, math

player_sprites = pygame.image.load("./assets/player_sprite.png")
brick_sprite = pygame.image.load("./assets/bricks.png")
yellow_tile_sprite = pygame.image.load("./assets/yellow_tile.png")
blue_tile_sprite = pygame.image.load("./assets/blue_tile.png")

terrain_scale = 16

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

def RenderGround(screen):
  width = math.floor(screen.get_width() / terrain_scale) - 2
  height = math.floor(screen.get_height() / terrain_scale) - 2

  for x in range(width):
    for y in range(height):
      if x % 2 == 0:
        RenderTile(screen, yellow_tile_sprite, pygame.Vector2(x + 1, y + 1))
      else:
        RenderTile(screen, blue_tile_sprite, pygame.Vector2(x + 1, y + 1))

def RenderTile(screen, img, pos):
  screen.blit(img, pos * terrain_scale)