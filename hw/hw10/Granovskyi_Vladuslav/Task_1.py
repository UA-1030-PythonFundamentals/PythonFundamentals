class Polygon:
    def __init__(self, sides):
        self.s = sides
        self.sides = [0 for i in range(sides)]

    def input_sides(self):
        self.sides = [float(input(str(i + 1))) for i in range(self.s)]

    def disp_sides(self):
        for i in range(self.s):
            print(i + 1, self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def find_area(self):
        s1, s2, s3 = self.sides
        s = (s1 + s2 + s3) / 2
        area = (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5
        print(area)


t = Triangle()
t.input_sides()
t.disp_sides()
t.find_area()