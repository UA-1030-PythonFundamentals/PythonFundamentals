class Polygon:
    def __init__(self,s1,s2):
        self.side1 = s1
        self.side2 = s2

    def frect(self):
        return self.side1*self.side2

class Rect(Polygon):
    pass
print(Rect(2, 2).frect())