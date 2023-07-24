class Person:

    def __init__(self, name, age):
        self.name = str(name)
        self.age = str(age)
        self.info = name + "s age is " + str(age)

    @property
    def get_info(self):
        return f"{self.name}s age is {self.age}"


person = Person("John Doe", 34)

print(person.info)
print(person.get_info)
