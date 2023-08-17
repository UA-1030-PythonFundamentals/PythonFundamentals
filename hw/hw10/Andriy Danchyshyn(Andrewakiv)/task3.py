class Employee:
    """Class to work with employee"""
    counter = 0

    def __init__(self, name, salary):
        self.__class__.counter += 1
        self.name = name
        self.salary = salary

    def info(self):
        return f'Name: {self.name} \n salary: {self.salary}'

    @classmethod
    def get_count_of_employee(cls):
        return f'Total number of employee: {cls.counter}'


john = Employee('John', 2500)
sue = Employee('Sue', 3000)
megan = Employee('Megan', 2000)

arr = [john, sue, megan]
for i in arr:
    print(i.info())
print(Employee.get_count_of_employee())


print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
