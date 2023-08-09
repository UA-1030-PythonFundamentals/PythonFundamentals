import math


def calculate_rectangle_area(length, width):
    """
    Calculates the area of a rectangle.

    Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width

def calculate_triangle_area(base, height):
    """
    Calculates the area of a triangle.

    Parameters:
        base (float): The base length of the triangle.
        height (float): The height of the triangle.

    Returns:
        float: The area of the triangle.
    """
    return 0.5 * base * height

def calculate_circle_area(radius):
    """
    Calculates the area of a circle.

    Parameters:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return math.pi * radius ** 2

def main():
    print("Choose a shape to calculate its area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate_rectangle_area(length, width)
        print("The area of the rectangle is:", area)
    elif choice == 2:
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = calculate_triangle_area(base, height)
        print("The area of the triangle is:", area)
    elif choice == 3:
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        print("The area of the circle is:", area)
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

