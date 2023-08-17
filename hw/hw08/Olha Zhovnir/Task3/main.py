from math import pi, pow
import formulas_for_area

def main():
    user_choice = input('If you want to calculate area of a:\nRectangular => enter 1,\nTriangle => enter 2,\nCircle => enter 3.\nPlease, make your choice:\n')

    match user_choice:
        case '1':
            a = float(input('Enter the length of the rectangular:'))
            b = float(input('Enter the width of the rectangular:'))
            formulas_for_area.rectangle_area(a,b)
        case '2':
            h = float(input('Enter the height of the triangle:'))
            a = float(input('Enter the base of the triangle:'))
            formulas_for_area.triangle_area(h,a)
        case '3':
            r = float(input('Enter the radius of the circle:'))
            formulas_for_area.circle_area(r)
        case _:
            print("Enter 1,2 or 3")

if __name__ == '__main__':
    main()
