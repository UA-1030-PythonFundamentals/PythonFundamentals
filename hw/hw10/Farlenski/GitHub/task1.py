class Polygon:
    pass


class Rectangle(Polygon):
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def square(self):
        return self.height * self.weight


rect = Rectangle(3, 4)
print(rect.square())
