import util, pygame, tile_class

current_room = []
    
def generateRoom(width, height):
    global current_room
  
    perlin = util.getPerlinNoise(10)

    room = []
    for x in range(width):
        row = []
        for y in range(height):
            if perlin[x][y] > 0.5:
                row.append(tile_class.Tile(pygame.Vector2(x,y), tile_class.TileTypes.Brick, collide=True))
            elif perlin[x][y] > 0.3:
                row.append(tile_class.Tile(pygame.Vector2(x,y), tile_class.TileTypes.BlueTile))
            else:
                row.append(tile_class.Tile(pygame.Vector2(x,y), tile_class.TileTypes.YellowTile))
        room.append(row)
                
    current_room = room

def RenderGround(screen):
  for x in range(len(current_room)):
    for y in range(len(current_room[x])):
      current_room[x][y].render(screen)