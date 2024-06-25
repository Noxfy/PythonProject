import pygame, sys, renderer

import util, player_class

player = player_class.Player()
  
def HandelEvents():
  for event in pygame.event.get():
    
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    player.Move(event)
  
def Render(screen):
  screen.fill((255, 255, 255))

  renderer.RenderGround(screen)
  player.Render(screen)

  pygame.display.update()

def Update():
  player.Update()