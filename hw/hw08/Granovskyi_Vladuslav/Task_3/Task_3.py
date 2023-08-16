from Area import rectangle, triangle, circle

Areas = input("Areas calculate (r, t, c):")

match(Areas):
    case "r":
        lenght = int(input("lenght="))
        width = int(input("width="))
        print(f"Area of rectangle is {rectangle(lenght, width)}")
    case "t":
        height = int(input("height="))
        side = int(input("side="))
        print(f"Area of triangle is {triangle(height, side)}")
    case "c":
        radius = int(input("radius="))
        print(f"Area of circle is {circle(radius)}")
