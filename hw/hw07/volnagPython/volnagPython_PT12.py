##Task2. Write a program that calculates the area of a rectangle,
##triangle and circle
##(write three functions to calculate the area, and call them in the
##main program depending on the user's choice). -- July 7,2023

print(70*"*")
shape = input('''Area of which geometrical figure you'd like to calculate?
(R -rectangle, T - triangle, C - circle)\n: ''')
PI = 3.14

if shape == "R":

    def main_pr(shape):
        
        dim1 = float(input("Enter it's width: \n"))
        dim2 = float(input("Enter it's height: \n"))
        a = dim1 * dim2
                
        return a
    
    print("***** AREA  OF  RECTANGLE :   ",main_pr(shape),end="\n")
elif shape == "T":

    def main_pr(shape):
        
        dim1 = float(input("Enter it's base: \n"))
        dim2 = float(input("Enter it's height: \n"))
        a = (dim1 * dim2)/2

        return a
    print("***** AREA  OF  TRIANGLE :   ",main_pr(shape),end="\n")
elif shape == "C":
    
    def main_pr(shape):
        
        rad = float(input("Enter the radius of it: \n"))
        a = PI*rad**2

        return a
    print("*****  AREA  OF  CIRCLE :   ",main_pr(shape),end="\n")
else:
    print("****** It's not known geometrical figure! *****" )
print(70*"*")
##VN
