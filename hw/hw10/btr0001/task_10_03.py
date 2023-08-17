class Employee:
    """The Employee class definition"""
    COUNTER = 0

    def __init__(self, name, salary):
        Employee.COUNTER += 1
        self.name = name
        self.salary = salary

    def __del__(self):
        Employee.COUNTER -= 1

    @staticmethod
    def info():
        print(f'Created {Employee.COUNTER} instances of Employee class')

    def emp_info(self):
        print(f'Salary of {self.name} is {self.salary}')

    @staticmethod
    def display_info():
        print(f"Base classes: {Employee.__base__}")
        print(f"Class namespace: {Employee.__dict__}")
        print(f"Class name: {Employee.__name__}")
        print(f"Module name: {Employee.__module__}")
        print(f"Documentation: {Employee.__doc__}")


emp1 = Employee('Jack', 3000)
emp2 = Employee('Jack', 3000)
emp1.info()
emp1.emp_info()
emp1.display_info()
