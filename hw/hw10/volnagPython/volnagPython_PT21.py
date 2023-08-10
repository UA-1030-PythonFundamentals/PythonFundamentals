##Task3. Create an employee class. Each employee has characteristics such as name
##and salary. The class should have a counter that calculates the total number of
##employees, as well as a method that prints the total number of employees and a
##method that displays information about each employee in particular, namely the
##name and salary.
##In addition to creating a class, display information about the base classes from which
##the employee class is inherited (__base__), the class namespace (__dict__), the
##class name (__name__), the module name in which the class is defined
##(__module__), the documentation bar ( __doc__) --HW11--PT21-- July 25,2023


class Factory:
    
    ''' This is  a Python class for all divisions at factory'''

    def __init__(self,factory,div1):
        self.div1 = div1
        self.factory = factory

    def __str__(self):
        return f" Factory {self.factory} has a division number {self.div1}."



class Employee(Factory):

    ''' This is a Python class for employees at factory'''

    num_emps = 0
    
    def __init__(self,name,salary):
        self.name =  name
        self.salary = salary

        Employee.num_emps += 1
        
    def __str__(self):
        return f"Employee {self.name} with salary in ${self.salary}."

    def display(self):
        return f"{self.name} has a salary of ${self.salary}."
##########################---Checking---##################################
t = Employee("Tom", 900) 
g = Employee("George", 600)    
w = Employee("Paul", 500)             # Instance of a the class "Employee"
print(70*"*")
print(Employee.display(w));print(Employee.display(t))
print(70*"*")
w.name
print(70*"*")
print("Number of empoyees at the factory :",Employee.num_emps)
print(70*"*")
###############---Information on the class---###################################
print("\nNamespace :",Employee.__dict__) 
print("\nPresent in the scope names :",dir()) 
print("\nThe class's name itself :",Employee.__name__)
print("\nThe name of the class's parent class :",Employee.__base__)
print("\nDiscription of the class :",Employee.__doc__)
print("\nName of defining module :",Employee.__module__)
#VN
