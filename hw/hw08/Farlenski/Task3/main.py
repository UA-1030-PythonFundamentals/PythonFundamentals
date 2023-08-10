from area import (rectangle,
                  triangle,
                  circle)


figure = input("Which figure you want to calculate(rectangle, triangle, circle): ")

match(figure):
    case "rectangle":
        a = int(input("Enter first side: "))
        b = int(input("Enter second side: "))
        print(f"Area of rectangle is {rectangle(a, b)}")
    case "triangle":
        h = int(input("Enter height: "))
        a = int(input("Enter side: "))
        print(f"Area of triangle is {triangle(h, a)}")
    case "circle":
        r = int(input("Enter the radius: "))
        print(f"Area of triangle is {circle(r)}")
    case _:
        print("This figure is not defined")