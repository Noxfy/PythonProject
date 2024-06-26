import pygame, sys, roomManager

import player_class, BulletManger, enemy_class

player = player_class.Player()
  
def HandelEvents():
  for event in pygame.event.get():
    
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      look_vector = (pygame.mouse.get_pos() - player.position).normalize()
      BulletManger.SpawnBullet(player.position + pygame.Vector2(0, 0), look_vector * 0.4)
  
def Render(screen):
  screen.fill((255, 255, 255))

  roomManager.RenderGround(screen)
  enemy_class.RenderEnemies(screen)
  player.Render(screen)
  BulletManger.RenderBullets(screen)

  pygame.display.update()

def Update():
  player.Update()
  BulletManger.UpdateBullets()
  if pygame.time.get_ticks() % 1000 == 0:
    enemy_class.enemies.append(enemy_class.Enemy(pygame.Vector2(0, 0)))
    print("spawned")
  enemy_class.UpdateEnemies(player)