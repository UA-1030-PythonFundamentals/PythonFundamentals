class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def get_area(self):
        raise NotImplementedError("Subclasses should implement this method.")

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)  
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

length_input = int(input("Enter the length of the rectangle: "))
width_input = int(input("Enter the width of the rectangle: "))

rectangle = Rectangle(length_input, width_input)
print(f"Rectangle area: {rectangle.get_area()}")
