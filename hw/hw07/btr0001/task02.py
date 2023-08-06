PI = 3.1415926


def triangle_area(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s


def rectangle_area(a, b):
    s = a * b
    return s


def circle_area(r):
    s = PI * r **2 / 4
    return s


a = input('Input object type (t - triangle, r - rectangle, c - circle): ')

match a:
    case 't':
        a = float(input('input 1st side: '))
        b = float(input('input 2nd side: '))
        c = float(input('input 3rd side: '))
        lst = [a, b, c].sort()
        if c >= a + b:
            print('wrong sides')
        else:
            print(f'Area of triangle is {triangle_area(a, b, c)}')
    case 'r':
        a = float(input('input 1st side: '))
        b = float(input('input 2nd side: '))
        print(f'Area of rectangle is {rectangle_area(a, b)}')
    case 'c':
        r = float(input('input 1st side: '))
        print(f'Area of circle is {circle_area(r)}')
    case _:
        print('Wrong type')

