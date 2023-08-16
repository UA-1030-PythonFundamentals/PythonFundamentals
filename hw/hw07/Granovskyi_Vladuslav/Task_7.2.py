a = input('Choose your area: ')

def areas():
    if a == 'r':
        print(area_rectangle())
    if a == 't':
        print(area_triangle())
    if a == 'c':
        print(area_circle())

def area_rectangle():
    length = float(input('Length: '))
    width = float(input('Width: '))
    return f'Area of your rectangle: {length * width}'

def area_triangle():
    base = float(input('Base: '))
    height = float(input('Height: '))
    return f'Area of your triangle: {0.5 * base * height}'

def area_circle():
    PI = 3.14
    radius = float(input('Radius: '))
    return f'Area of your circle: {PI * (radius ** 2)}'

print(areas())

