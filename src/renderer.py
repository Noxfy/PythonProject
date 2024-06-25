import pygame

player_sprites = pygame.image.load("./assets/player_sprite.png")

def RenderPlayer(screen, direction, player_position):
  screen.blit(player_sprites.subsurface(13 * direction.value, 0, 13, 17), player_position)
