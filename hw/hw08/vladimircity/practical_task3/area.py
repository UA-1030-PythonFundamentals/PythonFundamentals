# Write a program that calculates the area of a rectangle S=a*b, the area of a
# triangle S=0.5*h*a, the area of a circle S=pi*r**2. This module must be used in
# another module in which we ask the user the area of which figure he wants to
# calculate.

from math import pow, pi


def rectangle(a, b):
    s = a * b
    return round(s, 2)


def triangle(a, h):
    s = 0.5 * h * a
    return round(s, 2)


def circle(r):
    s = pi * pow(r, 2)
    return round(s, 2)
