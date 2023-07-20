# calculates the area of a rectangle, triangle, circle  

from math import pi

def rec(a, b):
    """area of a rectangle"""
    s = a * b
    return s

def tri(h, a):
    """area of a triangle"""
    s = 0.5 * h * a
    return s

def cir(r):
    """area of a circle"""
    s = pi * pow(r, 2)
    return float(round(s, 2))

