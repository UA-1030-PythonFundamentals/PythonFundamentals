##Create a module with functions of addition, subtraction,
##multiplication, division. And in another module - calculator.py, it is
##necessary to ask the user what action he wants to perform and
##with what numbers and perform the necessary actions. PT14 HW08 --- July 11,2023

from calculator import *


n1 = float(input("Enter your first number: \n"))
n2 = float(input("Enter your second number: \n"))
opr = input("Which math operation do you want to perform? \
A - addition, \
M - multiplication, \
D - division, \
S - subtraction :\n")


if opr == "A":
    su = ad(n1,n2)
    print("The result is: ", su)
elif opr == "M":
    pr = prd(n1,n2)
    print("The result is: ", pr)
elif opr == "D":
    di = dvs(n1,n2)
    print("The result is: ", di)
elif opr == "S":
    df = sbt(n1,n2)
    print("The result is: ", df)
else:
    
    print("***********Try another option****************")

#VN
