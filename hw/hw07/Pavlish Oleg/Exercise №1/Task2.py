def area_rectangle():
    '''This function calculates the area of rectangle!'''
    side1=float(input('Side #1: '))
    side2=float(input('Perpendicular side: '))
    return f'Area of your rectangle: {side1*side2}'
def area_triangle():
    '''This function calculates the area of triangle!'''
    base=float(input('Base: '))
    height=float(input('Height of triangle: '))
    return f'Area of your triangle: {base*height}'
def area_circle():
    '''This function calculates the area of circle!'''
    PI=3.14
    rad=float(input('Radius: '))
    return f'Area of your circle: {(rad**2)*PI}'
print(area_rectangle())
print(area_triangle())
print(area_circle())