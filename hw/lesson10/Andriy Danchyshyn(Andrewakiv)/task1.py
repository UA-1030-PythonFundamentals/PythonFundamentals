class Polygon:
    def __init__(self, sides):
        self.sides = sides


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(sides=4)
        self.length = length
        self.width = width

    def get_area(self):
        return f'Area {self.length*self.width}'


r = Rectangle(2, 4)
print(r.get_area())
