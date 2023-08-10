def rectangle(a, b):
    return f'area of rectangle: {a*b}'


def triangle(a, b):
    return f'area of triangle: {1/2*a*b}'


def circle(a):
    return f'area of circle: {3.14*a**2}'


choice = input('Choose a figure(rectangle/triangle/circle): ')
if choice == 'rectangle':
    a = int(input('width: '))
    b = int(input('height: '))
    print(rectangle(a, b))
elif choice == 'triangle':
    a = int(input('height: '))
    b = int(input('base: '))
    print(triangle(a, b))
else:
    a = int(input('radius: '))
    print(circle(a))
