import pygame, util

player_sprites = pygame.image.load("./assets/player_sprite.png")

#movemment variables
max_speed = 0.1
acceleration = 0.1
deceleration = 0.1

class Player:

  def __init__(self):
    self.player_state = util.PlayerDirection.North
    self.player_moving = False
    self.player_position = pygame.Vector2(64, 64)
    self.player_speed = 0.01
    self.velocity = pygame.Vector2(0,0)

  def Update(self):
    if (self.player_moving):
        #move player
        self.player_position += self.velocity

    
  def Render(self, screen):
    direction = 0

    angle = util.GetLookDirection(self.player_position)
    if (angle > -4 and angle < -2):
      direction = 0
    elif (angle < 0.5 and angle > -1):
      direction = 1
    elif (angle < -1 and angle > -2):
      direction = 3
    else:
      direction = 2

    screen.blit(player_sprites.subsurface(13 * direction, 0, 13, 17),
                self.player_position)

  def Move(self, event):
    keys = pygame.key.get_pressed()
    if event.type == pygame.KEYDOWN:
        player_move_vec = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(0,0)

        if keys[pygame.K_w]:
            player_move_vec.y -= 1
            self.player_moving = True
        if keys[pygame.K_d]:
            player_move_vec.x += 1
            self.player_moving = True
        if keys[pygame.K_s]:
            player_move_vec.y += 1
            self.player_moving = True
        if keys[pygame.K_a]:
            player_move_vec.x -= 1
            self.player_moving = True
        #normalize vector
        if player_move_vec.length() > 0:
            player_move_vec = player_move_vec.normalize()
        #apply acceleration or deceleration
        if player_move_vec.length() > 0:
            self.velocity += player_move_vec * acceleration
            if self.velocity.length() > max_speed:
                self.velocity = self.velocity.normalize() * max_speed
        else:
            if self.velocity.length() > 0:
                self.velocity -= self.velocity.normalize() * deceleration
                if self.velocity.length() < deceleration:
                    #self.velocity = pygame.Vector2(0, 0)
                    pass
        #print(self.velocity)
        
    if event.type == pygame.KEYUP and not (keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]):
        self.player_moving = False

    return self.velocity