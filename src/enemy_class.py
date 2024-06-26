import pygame, variables, random

enemies = []

class Enemy:
  def __init__(self, pos: pygame.Vector2):
    self.position = pos
    self.speed = 0.06

  def Render(self, screen):
    pygame.draw.circle(screen, (0, 200, 200), self.position + pygame.Vector2(random.randint(-2, 2),random.randint(-2, 2)), 10)

  def Update(self, target):
    self.move(target)

    #collision
    for other_enemy in enemies:
      if other_enemy != self and self.position.distance_to(other_enemy.position) < 10:
          # Apply separation force
          force_x = (self.position.x - other_enemy.position.x)
          force_y = (self.position.y - other_enemy.position.y)
          self.position.x += force_x 
          self.position.y += force_y
  

  def move(self, target):
    self.position += (target.position - self.position).normalize() * variables.scale * self.speed

def RenderEnemies(screen):
  for enemy in enemies:
    enemy.Render(screen)

def UpdateEnemies(player):
  for enemy in enemies:
    enemy.Update(player)


def SpawnWave(dificulty):
  border = 20
  for i in range(int(10 * dificulty)):
    position = pygame.Vector2(random.randint(-border, variables.width + border), random.randint(-border, variables.height + border))

    if position.x > variables.width and position.x < 0 and position.y > variables.height and position.y < 0:
      enemies.append(Enemy(position))
    else:
      i += 1
      print(i)