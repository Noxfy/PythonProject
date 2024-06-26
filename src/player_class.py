import pygame, util, variables

player_sprites = pygame.image.load("./assets/player_sprite.png")
player_sprite_size = pygame.Vector2(13, 17)


class Player:

    def __init__(self):
        self.direction = util.PlayerDirection.North
        self.is_moving = False
        self.position = pygame.Vector2(variables.width / 2, variables.width / 2)
        self.velocity = pygame.Vector2(0,0)
        self.speed = 0.08
        

    def Update(self):
        self.Move()

    
    def Render(self, screen):
        direction = 0

        angle = util.GetLookDirection(self.position)
        if (angle > -4 and angle < -2):
            direction = 0
        elif (angle < 0.5 and angle > -1):
            direction = 1
        elif (angle < -1 and angle > -2):
            direction = 3
        else:
            direction = 2

        screen.blit(pygame.transform.scale(player_sprites.subsurface(player_sprite_size.x * direction, 0, player_sprite_size.x, player_sprite_size.y), pygame.Vector2(variables.scale * player_sprite_size.x, variables.scale * player_sprite_size.y)), self.position - player_sprite_size * 0.5)

        #collision render debug
        #pygame.draw.rect(screen, (255, 0, 0), self.collider_rect, width=1)

    def Move(self):
        keys = pygame.key.get_pressed()
        player_move_vec = pygame.Vector2(0, 0)

        if keys[pygame.K_w]:
            player_move_vec.y -= 1
        if keys[pygame.K_d]:
            player_move_vec.x += 1
        if keys[pygame.K_s]:
            player_move_vec.y += 1
        if keys[pygame.K_a]:
            player_move_vec.x -= 1
        
        # Normalize vector
        if player_move_vec.length() > 0:
            player_move_vec = player_move_vec.normalize()
            self.velocity = player_move_vec * self.speed
        else:
            self.velocity = pygame.Vector2(0, 0)

        # Update player position

        sim_position = self.position + self.velocity * variables.scale
        if util.isCollidingWithTerrain(pygame.rect.Rect(sim_position.x, sim_position.y, player_sprite_size.x * variables.scale, player_sprite_size.y * variables.scale)) == None:
            self.position = sim_position
