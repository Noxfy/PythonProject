import pygame

import util, variables
bullets = []

class Bullet:

  def __init__(self, position, velocity, damage=1):
    self.damage = damage
    self.position = position
    self.velocity = velocity

  def render(self, screen):
    pygame.draw.circle(screen, (255, 0, 0), self.position, 10 * variables.scale)

  def update(self):
    if util.OutOfBounds(self.position):
      bullets.remove(self)
    
    self.position += self.velocity * variables.scale


def SpawnBullet(position, velocity):
  bullets.append(Bullet(position, velocity))


def UpdateBullets():
  for bullet in bullets:
    bullet.update()


def RenderBullets(screen):
  for bullet in bullets:
    bullet.render(screen)
