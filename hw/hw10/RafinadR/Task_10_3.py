class Human:
    
    def __init__(self, name):
        self.name = name
        

class Employee(Human):
    counter = 0

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
        Employee.counter += 1
       
    def worker_info(self):
        return f"Name: {self.name} --- Salary: {self.salary}"
   

worker1 = Employee(input("Enter name:\n"), input("Enter salary:\n"))
worker2 = Employee(input("Enter name:\n"), input("Enter salary:\n"))
worker3 = Employee(input("Enter name:\n"), input("Enter salary:\n"))


print("Number of employees -", Employee.counter)

print(worker1.worker_info())
print(worker2.worker_info())
print(worker3.worker_info())

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)




