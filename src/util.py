import math


def normalize(arr):
    norm_arr = [None, None]
    length = math.sqrt(arr[0] * arr[0] + arr[1] * arr[1])
    norm_arr[0] = arr[0] / length
    norm_arr[1] = arr[1] / length
    return norm_arr
