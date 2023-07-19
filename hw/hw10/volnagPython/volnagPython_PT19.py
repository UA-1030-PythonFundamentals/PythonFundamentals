##Task1. Create a polygon class and a rectangle class
##that inherits from the polygon class and finds the square
##of rectangle.-- HW10 -- PT19-- July 19, 2023

###########################----Base class-----############################# 
class polygon:

    
    def __init__(self,shape,side1,side2,side3,side4,side5): #Initializing a class
        self.shape = shape                  #Parameters of a class
        self.side1 = side1                  #Parameters of a class
        self.side2 = side2                  #Parameters of a class
        self.side3 = side3
        self.side4 = side4
        self.side4 = side4
        
    def __str__(self):
        return f"{self.shape} with many sides "

    def geometry(self):             #Defining methods or functions in this class#
        print("This is a " + self.shape.upper())


 
###########################----Interited class-----#####################################
        

class rectangle(polygon):

    
       def __init__(self,shape,side1,side2): #Initializing a class
           self.shape = shape
           self.side1 = side1
           self.side2 = side2

       def __str__(self):
           return f"{self.shape} with two sides "

       def area(self):
           a = self.side1*self.side2
           print(f"The area of {self.shape} is {a} cm^2")

        
###########################-----Checking results---#####################################

r = rectangle("Rectangle",15,19)    # Object with attributes i.e. "shape,side etc."
print(r)
print(r.side1)
print(r.side2)
print(r.shape)
r.area()

