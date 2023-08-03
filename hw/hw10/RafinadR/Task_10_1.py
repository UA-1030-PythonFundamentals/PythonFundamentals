class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input(f"Enter side {str(i+1)}: ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print(f"Side {i+1} is {self.sides[i]}")


class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 4)

    def findArea(self):
        a, b, c, d = self.sides
        if a == c and b == d:
            s = a * b
            print(f"The area of rectangle with width {a} and length {b} is {s}")
        else:
            print("The entered sides do not form a rectangle")

r = Rectangle()
r.inputSides()
r.dispSides()
r.findArea()