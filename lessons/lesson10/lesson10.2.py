# class A:
#     def __init__(self):
#         print("__init__A")
# class Singleton:
#     __obj = None  # attribute for storing a single copy
#
#     def __new__(cls, *args, **kwargs):  # class Singleton.
#         print("__new__Singleton")
#         if cls.__obj is None:
#             # If it does not yet exist, then
#             # call __new__ of the parent class
#             # cls.__obj = object.__new__(A, *args, **kwargs)
#             cls.__obj = object.__new__(cls, *args, **kwargs)
#         return cls.__obj  # will return Singleton
#     def __init__(cls, *args, **kwargs):  # class Singleton.
#         print("__init__Singleton")
#
# o1 = Singleton()
# print(id(o1), type(o1))
# o2 = Singleton()
# print(id(o2), type(o2))
# o3 = Singleton()
# print(id(o3))
#
# class Point:
#     def __init__(self, x=0, y=0):
#         print("init_Point")
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"x={self.x} y={self.y}"
#
#     def __repr__(self):
#         return f"({self.x},{self.y})"
#
#     def set_x(self, x):
#         self.x = x
#
#     def get_x(self):
#         return self.x
#
#     def set_y(self, y):
#         self.y = y
#
#     def get_y(self):
#         return self.y
#
#
# p1 = Point()
# p2 = Point(1, 9)
# p3 = Point(-3, -7)
#
# print(p1, p2, p3)
# print([p1, p2, p3])
#
#
# class Point3d(Point):
#     def __init__(self, x=0, y=0, z=0):
#         print("init_Point3D")
#         super().__init__(x, y)
#         self.z = z
#
#     def __str__(self):
#         return f"{super().__str__()} z={self.z}"
#
#     def __repr__(self):
#         return f"({self.x},{self.y},{self.z})"
#
#     def get_z(self):
#         return self.z
#
#     def set_z(self, z):
#         self.z = z
#
#
# p3d = Point3d(1, 2, 3)
# print(p3d)
# p3d.set_x(99)
# print([p3d])
#
#
# print(isinstance(p1, Point))
# print(isinstance(p3d, Point))
#
#
# print(issubclass(Point3d, Point))
# print(issubclass(Point, Point3d))

#
# class A: pass
#
#
# class B(A): pass
#
#
# class C(A): pass
#
#
# class D(B, C): pass
#
# class G(A):pass
#
# class E(G, D): pass
#
#
# class F(G, C): pass
#
#
# f = F()
# print(F.__mro__)
# print(E.__mro__)

#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"x={self.x} y={self.y}"
#
#     def __repr__(self):
#         return f"({self.x},{self.y})"
#
#     def set_x(self, x):
#         self.x = x
#
#     def get_x(self):
#         return self.x
#
#     def set_y(self, y):
#         self.y = y
#
#     def get_y(self):
#         return self.y
#
#
# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.p1 = Point(x1, y1)
#         self.p2 = Point(x2, y2)
#
#     def __str__(self):
#         return f"{self.p1} {self.p2}"
#
#     def distance(self):
#         print(type(self))
#         return ((self.p1.get_x() - self.p2.get_x()) ** 2 + (self.p1.get_y() - self.p2.get_y()) ** 2) ** 0.5
#
#     @classmethod
#     def get_class_name(cls):
#         print(type(cls))
#         return cls.__name__
#
#     @staticmethod
#     def my_f():
#         print("static")
#
#
# l = Line(1, 1, 2, 2)
# print(l)
# print(l.distance())
# print(Line.distance(l))
# print(l.get_class_name())
# print(Line.get_class_name())
# print(l.my_f())
# print(Line.my_f())

# class A:
#     def __init__(self, a1=0, a2=0, a3=0):
#         self.a = a1
#         self._a = a2
#         self.__a = a3
#
#     def __str__(self):
#         # return f"{self.a} {self._a} {self.__a}"
#         return self.__my()
#     def __my(self):
#         return f"{self.a} {self._a} {self.__a}"
#
#
# a = A(1, 2, 3)
# print(a)
# print(a.a)
# print(a._a)
# print(a._A__a)
# print(a._A__my())


# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"x={self.__x} y={self.__y}"
#
#     def __repr__(self):
#         return f"({self.__x},{self.__y})"
#
#     def set_x(self, x):
#         self.__x = x
#
#     def get_x(self):
#         print("get_x")
#         return self.__x
#
#     def set_y(self, y):
#         self.__y = y
#
#     def get_y(self):
#         return self.__y
#
# p = Point(15, 25)
# print(p)
# p._Point__x = -37
# p._Point__y = -45
# print(p, p.get_x(), p.get_y())
# p.set_x(88)
# p.set_y(99)
# print(p, p.get_x(), p.get_y())


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"x={self.__x} y={self.__y}"

    def __repr__(self):
        return f"({self.__x},{self.__y})"

    def _set_x(self, x):
        print("set_x", x)
        self.__x = x

    def _get_x(self):
        print("get_x")
        return self.__x

    x = property(_get_x, _set_x, doc="property for x")

    @property
    def y(self):
        print("get_y")
        return self.__y

    @y.setter
    def y(self, y):
        print("set_y")
        self.__y = y


p = Point(1, 2)
p.x = 15
print(p.x)
p.y = 25
print(p.y)
