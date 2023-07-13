# Task2. Write a program that calculates the area of a rectangle, triangle and circle
# (write three functions to calculate the area. And call them in the main program
# depending on the user's choice).
import math


def rectangle():
    x = float(input('Enter first side: '))
    y = float(input('Enter second side: '))
    area = x * y
    return round(area, 2)


def triangle():
    a = float(input('Enter first side: '))
    b = float(input('Enter second side: '))
    c = float(input('Enter third side: '))
    s = (a + b + c) / 2  # semi-perimeter
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return round(area, 2)


def circle():
    r = float(input('Enter radius: '))
    area = r ** 2 * math.pi
    return round(area, 2)


def main():
    match input('Enter the figure (rectangle, triangle or circle): '):
        case 'rectangle':
            print('Area =', rectangle())
        case 'triangle':
            print('Area =', triangle())
        case 'circle':
            print('Area =', circle())
        case _:
            print('You should enter "rectangle", "triangle" or "circle"')


if __name__ == '__main__':
    main()


