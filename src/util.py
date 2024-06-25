import math


def normalize_vector(vector):
    x, y = vector
    magnitude = math.sqrt(x**2 + y**2)
    
    if magnitude == 0:
        raise ValueError("Cannot normalize a zero vector")
    
    normalized_vector = [x / magnitude, y / magnitude]
    return normalized_vector
