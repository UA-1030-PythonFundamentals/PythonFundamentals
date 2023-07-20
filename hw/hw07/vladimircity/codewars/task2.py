# Find The Distance Between Two Points
from math import sqrt


def distance(x1, y1, x2, y2):
    a = x1 - x2
    b = y1 - y2
    c = sqrt(a ** 2 + b ** 2)
    return round(c, 2)


print(distance(1, 1, 0, 0))
