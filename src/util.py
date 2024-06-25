import math, pygame

def normalize_vector(vector):
    x, y = vector
    magnitude = math.sqrt(x**2 + y**2)
    
    if magnitude == 0:
        raise ValueError("Cannot normalize a zero vector")
    
    normalized_vector = [x / magnitude, y / magnitude]
    return normalized_vector

def GetLookDirection(player_pos):
    mouse_pos = pygame.mouse.get_pos()

    vec2 = [None, None]
    vec2[0] = mouse_pos[0] - player_pos[0]
    vec2[1] = mouse_pos[1] - player_pos[1]
    vec1 = [0, 1]

    #angle_to_mouse = math.atan((mouse_pos[0] - player_pos[0]) / (mouse_pos[1] - player_pos[1])) * (180/math.pi)
    angle_to_mouse = math.atan2(vec2[1], vec2[0]) - math.atan2(vec1[1], vec1[0])

    print(angle_to_mouse)
    return angle_to_mouse