import pygame, variables
from enum import Enum

brick_sprite = pygame.image.load("./assets/bricks.png")
yellow_tile_sprite = pygame.image.load("./assets/yellow_tile.png")
blue_tile_sprite = pygame.image.load("./assets/blue_tile.png")

class TileTypes(Enum):
    Brick = 0
    BlueTile = 1
    YellowTile = 2

tiles_with_collision = [TileTypes.Brick]

class Tile:
    def __init__(self, pos, disp=TileTypes.YellowTile, collide=False, health=1):
        self.display = disp
        self.health = health
        self.tile_position = pos
        self.has_collision = collide

    def render(self, screen):
        match(self.display):
            case TileTypes.Brick:
                screen.blit(pygame.transform.scale(brick_sprite, pygame.Vector2(variables.terrain_scale, variables.terrain_scale)), self.tile_position * variables.terrain_scale)
            case TileTypes.YellowTile:
                screen.blit(pygame.transform.scale(yellow_tile_sprite, pygame.Vector2(variables.terrain_scale, variables.terrain_scale)), self.tile_position * variables.terrain_scale)
            case TileTypes.BlueTile:
                screen.blit(pygame.transform.scale(blue_tile_sprite, pygame.Vector2(variables.terrain_scale, variables.terrain_scale)), self.tile_position * variables.terrain_scale)

