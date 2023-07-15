from tools import rectangle_area, triangle_area, circle_area

a = input('Input object type (t - triangle, r - rectangle, c - circle): ')

match a:
    case 't':
        a = float(input('input a length of base: '))
        h = float(input('input a length of height: '))
        print(f'Area of triangle is {triangle_area(a, h)}')
    case 'r':
        a = float(input('input 1st side: '))
        b = float(input('input 2nd side: '))
        print(f'Area of rectangle is {rectangle_area(a, b)}')
    case 'c':
        r = float(input('input radius: '))
        print(f'Area of circle is {circle_area(r)}')
    case _:
        print('Wrong type')