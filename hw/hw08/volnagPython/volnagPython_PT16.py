##Task3.
##Write a program that calculates the area of a rectangle S=a*b, the area of a
##triangle S=0.5*h*a, the area of a circle S=pi*r**2. This module must be used in
##another module in which we ask the user the area of which figure he wants to
##calculate.
##(To perform the task, you need to import the math module, and from it the
##pow() function and the value of the variable pi, and module, which contains
##three functions for finding areas, into the main program. The basic logic of the
##program is executed in the main module). -- HW08  PT16 ---July 11, 2023

from area import *


print(70*"*")
shape = input('''Area of which geometrical figure you'd like to calculate?
(R -rectangle, T - triangle, C - circle)\n: ''')

if shape == "R":
    dim1 = float(input("Enter it's width: \n"))
    dim2 = float(input("Enter it's height: \n"))
    a = main_r(dim1,dim2)
    print("***** AREA  OF  RECTANGLE :   ", a,end="\n")
elif shape == "T":
    dim1 = float(input("Enter it's base: \n"))
    dim2 = float(input("Enter it's height: \n"))
    a = main_tr(dim1,dim2)
    print("***** AREA  OF  TRIANGLE :   ", a,end="\n")
elif shape == "C":
    rad = float(input("Enter the radius of it: \n"))
    a = main_c(rad)        
    print("*****  AREA  OF  CIRCLE :   ", a,end="\n")
else:
    print("****** It's not known geometrical figure! *****" )
print(70*"*")

##VN
