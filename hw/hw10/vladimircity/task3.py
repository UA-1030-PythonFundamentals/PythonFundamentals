class Employee:
    """This is the Employee class."""
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def print_employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @staticmethod
    def print_total_employees():
        print(f"Total employees: {Employee.total_employees}")


employee1 = Employee("John Doe", 50000)
employee2 = Employee("Jane Smith", 60000)

employee1.print_employee_info()
employee2.print_employee_info()
Employee.print_total_employees()

print("Base classes:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)
