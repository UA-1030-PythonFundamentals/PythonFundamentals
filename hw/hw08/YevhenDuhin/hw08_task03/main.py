from hw08_task03 import *
def main():
    print("Select a figure to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    choice = input("Your choice (1-3): ")

    if choice == '1':
        a = float(input("Enter the length of side A of the rectangle: "))
        b = float(input("Enter the length of side B of the rectangle: "))
        area = calculate_rectangle_area(a, b)
        print("Area of the rectangle: ", area)
    elif choice == '2':
        a = float(input("Enter the length of the base of the triangle: "))
        h = float(input("Enter the height of the triangle: "))
        area = calculate_triangle_area(a, h)
        print("Area of the triangle: ", area)
    elif choice == '3':
        r = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(r)
        print("Circle area: ", area)
    else:
        print("Incorrect choice.")

if __name__ == "__main__":
    main()
