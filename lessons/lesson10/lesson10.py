names = []
ages = []
phones = []
sex = []


#
# class Human:
#     """Represent a human"""
#     cm = []
#     ci = ""
#     def __init__(self):
#         self.im = []
#         self.ii = 15
#     def __str__(self):
#         return f"cm:{self.cm} ci:{self.ci} im:{self.im} ii:{self.ii}"
#
# h1 = Human()
# h2 = Human()
# print(id(h1), type(h1), h1)
# print(id(h2), type(h2), h2)
# h1.cm.append("test1")
# h2.ci = 99
# h1.im.append("test2")
# h1.im = 88
# print(id(h1), type(h1), h1)
# print(id(h2), type(h2), h2)

#
# class Human:
#     def __init__(self, name, age, phone, sex):
#         self.name = name
#         self.age = age
#         self.phone = phone
#         self.sex = sex
#
#     def __del__(self):
#         print("delete", id(self), self)
#     def __str__(self):
#         return f"{self.name} {self.age} {self.phone} {self.sex}"
#
#     def my_print(d):
#         print(f"""{d.name=}\n
#         {d.age=}\n
#         {d.phone=}\n
#         {d.sex=}\n""")
#
# h1 = Human("A", 18, 9999999, "maly")
# h2 = Human("b", 86, 9999999, "maly")
# h1.my_print()
# h2.my_print()
#
# def print_name(obj):
#     print(obj.name)
#
# print_name(h1)
#
# Human.get_name = print_name
#
# h1.get_name()
#
# f = Human.my_print
# f(h2)
# print(dir(h1))
# print(h1.__dict__)
# print(Human.__dict__)

# class Point:
#     def __init__(self, x=0, y=0):
#         self._x = x
#         self._y = y
#
#     def add(self, point):
#         p = Point()
#         p._x = self._x + point._x
#         p._y = self._y + point._y
#         return p
#     def __del__(self):
#         print("delete: ", id(self), self)
#     def __add__(self, other):
#         p = Point()
#         p._x = self._x + other._x
#         p._y = self._y + other._y
#         return p
#
#     def __eq__(self, other):
#         if type(other) == Point:
#             return self._x == other._x and self._y == other._y
#         elif type(other) == int or type(other) == float:
#             return self._x + self._y == other
#
#     def __lt__(self, other):
#         s = (self._x ** 2 + self._y ** 2) ** 0.5
#         o = (other._x ** 2 + other._y ** 2) ** 0.5
#         return s < o
#
#     def __str__(self):
#         return f"x:{self._x} y:{self._y}"
#
#     def __repr__(self):
#         return f"({self._x}:{self._y})"
#
#
#
#
# p1 = Point()
# p2 = Point(-1, -1)
# p3 = Point(-5, 3)
# p41 = p2.add(p3)
# print(p41)
# p42 = p3 + p2
# print(p42)
# print(p42 == 10)
# print(p42 == p41)
# print(p42 == p2)
# s = str(p2)
# points = [p3, p41, p42, p1, p2, ]
# print(points)
# points.sort()
# del p1
# p2 = Point(99, 99)
# points[1] = p2
# print(points)

class B:
    def __init__(self, z=0):
        self.z = z
class A:

    def __init__(self, x, z=1):
        self.x = x
        self.b = B()
    def __str__(self):
        return f"x:{self.x} b:{self.b.z}"

a = A(1)
print(a)

# b = B()
b = A.B()
print(b)