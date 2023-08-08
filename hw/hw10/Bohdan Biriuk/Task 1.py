class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def input_sides(self):
        self.sides = [float(input(f"Enter side {str(i+1)}: "))
                      for i in range(self.n)]

    def disp_Sides(self):
        for i in range(self.n):
            print(f"Side {i+1} is {self.sides[i]} ")


class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)

    def find_area(self):
        a, b = self.sides
        s = a * b
        print(f"Area of rectangle = {s}")

test = Rectangle()
test.input_sides()
test.disp_Sides()
test.find_area()



