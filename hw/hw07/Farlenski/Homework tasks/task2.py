from math import sqrt, pi


def rectangle(width, height):
    """Area of a rectangle"""
    return width * height


def triangle(side1, side2, side3):
    """Area of a triangle"""
    p = (side1 + side2 + side3) / 2
    return sqrt(p * (p - side1) * (p - side2) * (p - side3))


def circle(radius):
    """Area of a circle"""
    return pi * (radius ** 2)


match input('Enter the figure (rectangle, triangle or circle) or exit: '):
    case 'rectangle':
        print('Area =', rectangle(float(input("Enter the width: ")),
                                  float(input("Enter the height: "))))
    case 'triangle':
        print('Area =', triangle(float(input("Enter first side: ")),
                                 float(input("Enter second side: ")),
                                 float(input("Enter third side: "))))
    case 'circle':
        print('Area =', circle(float(input("Enter first radius: "))))
    case _:
        print('Please, enter "rectangle", "triangle" or "circle" or exit')
