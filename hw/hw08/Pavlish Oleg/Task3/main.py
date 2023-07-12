from calculates import *
choice=input('Let\'s calculate of Rectangle/Triangle/Circle: ')
match choice:
    case 'Rectangle':
        side1=int(input('First side: '))
        side2=int(input('Second side: '))
        print(area_rect(side1,side2))
    case 'Triangle':
        height=int(input('Height: '))
        base=int(input('Base: '))
        print(area_triangle(height,base))
    case 'Circle':
        radius=int(input('Radius: '))
        print(area_circle(radius))