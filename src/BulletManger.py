import pygame

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
      tile_health = collision[1] - self.damage
      self.damage -= collision[1]
      if self.damage <= 0:
        bullets.remove(self)
      
      if tile_health <= 0:
        collision = collision[0]
        roomManager.rects.remove(collision)
        roomManager.current_room[int(collision.x / variables.terrain_scale)][int(collision.y / variables.terrain_scale)] = 2
      else:
        #asdasfasfkajsdflkajsldjals kjlk fix tile heal;th
      
      

def SpawnBullet(position, velocity):
  bullets.append(Bullet(position, velocity))


def UpdateBullets():
  for bullet in bullets:
    bullet.update()


def RenderBullets(screen):
  for bullet in bullets:
    bullet.render(screen)
