def area_rectangle():
    length = float(input('length: '))
    width = float(input('width: '))
    area = length * width
    return f'Area of your rectangle: {area}'

def area_triangle():
    base = float(input('Base: '))
    height = float(input('Height: '))
    area = 0.5 * base * height
    return f'Area of your triangle: {area}'

def area_circle():
    PI = 3.14
    radius = float(input('Radius: '))
    area = PI * (radius ** 2)
    return f'Area of your circle: {area}'

print(area_rectangle())
print(area_triangle())
print(area_circle())
