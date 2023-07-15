from math import pow, pi


def triangle_area(base, h):
    s = base * h / 2
    return s


def rectangle_area(a, b):
    s = a * b
    return s


def circle_area(rad):
    s = pi * pow(rad, 2) / 4
    return s

