import pygame

from tile_class import Tile, TileTypes
import util, variables, roomManager
bullets = []

class Bullet:

  def __init__(self, position, velocity, damage=1, size=5):
    self.damage = damage
    self.position = position
    self.velocity = velocity
    self.size = size

  def render(self, screen):
    pygame.draw.circle(screen, (255, 255, 255), self.position, self.size * variables.scale)

  def update(self):
    if util.OutOfBounds(self.position):
      bullets.remove(self)
    
    self.position += self.velocity * variables.scale

    #COLLISION
    collision = util.isCollidingWithTerrain(pygame.rect.Rect(self.position.x, self.position.y, self.size * variables.scale, self.size * variables.scale))

    if collision != None:
      hp = collision.health
      collision.health -= self.damage
      self.damage -= hp
      if self.damage <= 0:
        bullets.remove(self)
      if collision.health <= 0:
        t = Tile(collision.tile_position, TileTypes.BlueTile, collide=False)
        roomManager.current_room[int(collision.tile_position.x)][int(collision.tile_position.y)] = t
        
      
      

def SpawnBullet(position, velocity):
  bullets.append(Bullet(position, velocity))


def UpdateBullets():
  for bullet in bullets:
    bullet.update()


def RenderBullets(screen):
  for bullet in bullets:
    bullet.render(screen)
