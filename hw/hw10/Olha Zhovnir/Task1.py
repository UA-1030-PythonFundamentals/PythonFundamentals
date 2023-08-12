class Polygon:
    def __init__(self,number_of_sides):
        self.n = number_of_sides
        self.sides = [0 for i in range(number_of_sides)]

    def input_sides(self):
        self.sides = [float(input(f'Enter a side {str(i+1)}: ')) for i in range(self.n)]

    def disp_sides(self):
        for i in range(self.n):
            print(f'Side {i+1} is {self.sides[i]}')

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)
    def rectangle_area(self):
        a,b = self.sides
        area = a*b
        print(f'The area of the rectangle is {area}')

r = Rectangle()
r.input_sides()
r.disp_sides()
r.rectangle_area()