import pygame, util, math, variables, roomManager

player_sprites = pygame.image.load("./assets/player_sprite.png")

brick_sprite = pygame.image.load("./assets/bricks.png")
yellow_tile_sprite = pygame.image.load("./assets/yellow_tile.png")
blue_tile_sprite = pygame.image.load("./assets/blue_tile.png")


def RenderGround(screen):
  width = math.floor(variables.width / variables.terrain_scale)
  height = math.floor(variables.height / variables.terrain_scale)

  ground = roomManager.current_room

  for x in range(width):
    for y in range(height):
      if ground[x][y] == 0:
        RenderTile(screen, blue_tile_sprite, pygame.Vector2(x, y)) 
      elif ground[x][y] == 1:
        RenderTile(screen, yellow_tile_sprite, pygame.Vector2(x, y)) 
      elif ground[x][y] == 2:
        RenderTile(screen, brick_sprite, pygame.Vector2(x, y)) 
  
  for rect in roomManager.rects:
    pygame.draw.rect(screen, (255, 0, 0), rect[0], width=1)

def RenderTile(screen, img, pos):
  screen.blit(pygame.transform.scale(img, pygame.Vector2(variables.terrain_scale, variables.terrain_scale)), pos * variables.terrain_scale)