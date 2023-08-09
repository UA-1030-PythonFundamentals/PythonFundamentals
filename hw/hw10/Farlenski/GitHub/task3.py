class Employee:
    __numbers_of_employee = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.__numbers_of_employee += 1

    @staticmethod
    def get_total():
        print(f"The total number of employees: {Employee.__numbers_of_employee}")

    def get_information(self):
        print(f"Name: {self.name}, "
              f"Salary: {self.salary}")


employee_1 = Employee("Nick", 1000)
employee_2 = Employee("Vita", 2000)
employee_3 = Employee("Roma", 500)

Employee.get_total()
employee_1.get_information()
employee_2.get_information()
employee_3.get_information()
print()

print(f"The base class: {Employee.__base__},\n"
      f"The class namespace: {Employee.__dict__},\n"
      f"The class name: {Employee.__name__}\n"
      f"The module name: {Employee.__module__}\n"
      f"The documentation bar: {Employee.__doc__}")