import area

def get_area():
    figure = input("Choose figure (rectangle, triangle, circle): ")
    match figure:
        case "rectangle":
            a = float(input("Entar side a: "))
            b = float(input("Enter side b: "))
            print("Area = ", area.rectangle(a, b))
        case "triangle":
            h = float(input("Enter h: "))
            a = float(input("Enter side a: "))
            print("Area =", area.triangle(h, a))
        case "circle":
            r = float(input("Enter r: "))
            print("Area = ", area.circle(r))

test = get_area()
print(test)
