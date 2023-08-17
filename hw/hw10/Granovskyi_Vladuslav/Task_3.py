class Employee:
    counter = 0

    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary

    def __del__(self):
        Employee.counter -= 1

    @staticmethod
    def information():
        print(f'Created {Employee.counter} instances of Employee class')

    def emp_information(self):
        print(f'Salary of {self.name} is {self.salary}')

    @staticmethod
    def display_information():
        print(f"Base classes: {Employee.__base__}")
        print(f"Class namespace: {Employee.__dict__}")
        print(f"Class name: {Employee.__name__}")
        print(f"Module name: {Employee.__module__}")
        print(f"Documentation: {Employee.__doc__}\n")

emp1 = Employee('Villson', 2300)
emp1.information()
emp1.emp_information()
emp1.display_information()
emp2 = Employee('Dan', 2300)
emp2.information()
emp2.emp_information()
emp2.display_information()