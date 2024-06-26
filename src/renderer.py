import pygame, util, math, variables

player_sprites = pygame.image.load("./assets/player_sprite.png")
brick_sprite = pygame.image.load("./assets/bricks.png")
yellow_tile_sprite = pygame.image.load("./assets/yellow_tile.png")
blue_tile_sprite = pygame.image.load("./assets/blue_tile.png")

terrain_scale = 16 * variables.scale

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
  screen.blit(pygame.transform.scale(img, pygame.Vector2(terrain_scale, terrain_scale)), pos * terrain_scale)