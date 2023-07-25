class Employee:
    quantity=0
    def __init__(self,name,salary):
        self.name=name
        Employee.quantity+=1
        self.salary=salary

    def total_emp(self, q=quantity):
        print(f'Total quantity: {q}')

    def __str__(self):
        return f'INFO BAR: Name of employee: {self.name}, Salary: {self.salary}'

emp_Jordan=Employee('Jordan', 3000)
emp_Rick=Employee('Rick', 2500)
emp_Edward=Employee('Edward', 2800)
print(Employee.quantity)

print(emp_Jordan)
print(emp_Rick)
print(emp_Edward)