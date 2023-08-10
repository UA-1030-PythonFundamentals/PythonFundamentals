# Write a program that calculates the area of a rectangle S=a*b, the area of a
# triangle S=0.5*h*a, the area of a circle S=pi*r**2. This module must be used in
# another module in which we ask the user the area of which figure he wants to
# calculate.
#
# (To perform the task, you need to import the math module, and from it the
# pow() function and the value of the variable pi, and module, which contains
# three functions for finding areas, into the main program. The basic logic of the
# program is executed in the main module).


import area


def main():
    figure = input('Choose the figure (1 rectangle, 2 triangle, 3 circle):')
    match figure:
        case '1':
            a = float(input('Enter side a: '))
            b = float(input('Enter side b: '))
            print('Area =', area.rectangle(a, b))
        case '2':
            a = float(input('Enter side a: '))
            h = float(input('Enter h: '))
            print('Area =', area.triangle(a, h))
        case '3':
            r = float(input('Enter radius r: '))
            print('Area =', area.circle(r))
        case _:
            print('You should enter 1, 2 or 3')


if __name__ == '__main__':
    main()
