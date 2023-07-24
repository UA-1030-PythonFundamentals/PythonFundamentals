class Polygon:
    def __init__(self, side_lengths):
        self.side_lengths = side_lengths


class Rectangle(Polygon):
    def area(self):
        return self.side_lengths[0] * self.side_lengths[1]  # Area = length * width


if __name__ == "__main__":
    rectangle = Rectangle([5, 10])
    print("Area:", rectangle.area())
