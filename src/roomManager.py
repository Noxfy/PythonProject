import math, util, pygame, variables

current_room = []
rects = []

    
def generateRoom(width, height):
    global current_room
  
    perlin = util.getPerlinNoise(10)

    rect_count = 0

    room = []
    for x in range(width):
        row = []
        for y in range(height):
            if perlin[x][y] > 0.5:
                row.append(0)
                temp = []
                temp.append(pygame.rect.Rect(x * variables.terrain_scale, y * variables.terrain_scale, variables.terrain_scale, variables.terrain_scale))
                temp.append(2)
                temp.append(rect_count)
                rect_count += 1
                rects.append(temp)
            elif perlin[x][y] > 0.3:
                row.append(1)
            else:
                row.append(2)
        room.append(row)
                
    current_room = room