# area of circle pi r^2

import math

def score(x, y):
    sq_root = math.sqrt((x ** 2) + (y ** 2))
    if sq_root > 10:
        return 0
    elif sq_root > 5:
        return 1
    elif sq_root > 1:
        return 5
    else:
        return 10
