class Employee:
    counter = 0
    def __init__(self, name, salary):
        self.__class__.counter +=1
        self.name = name
        self.salary = salary

    def info(self):
        return (f"Employee {self.name}, have salary: {self.salary}")

    @classmethod
    def get_count(cls):
        return (f"Total number of employee: {cls.counter}")


Dan = Employee("Dan", 4500)
Lisa = Employee("Lisa", 4000)
Bob = Employee("Bob", 4200)
Zoe = Employee("Zoe", 3500)

all = [Dan, Lisa, Bob, Zoe]
for i in all:
    print(i.info())
print(Employee.get_count())


print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)