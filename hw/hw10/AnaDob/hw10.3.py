class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"

    @classmethod
    def display_total_employees(cls):
        return f"Total Employees: {cls.total_employees}"

    @staticmethod
    def display_class_info():
        class_info = f"Base classes: {Employee.__base__}\n"
        class_info += f"Class namespace: {Employee.__dict__}\n"
        class_info += f"Class name: {Employee.__name__}\n"
        class_info += f"Module name: {Employee.__module__}\n"
        class_info += f"Documentation: {Employee.__doc__}"
        return class_info

