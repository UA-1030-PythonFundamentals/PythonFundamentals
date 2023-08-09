class Person:
    def __init__(self, name, age=0):
        self.__name = name
        self.__age = age

    @property
    def get_info(self):
        return f"{self.__name}s age is {self.__age}"


