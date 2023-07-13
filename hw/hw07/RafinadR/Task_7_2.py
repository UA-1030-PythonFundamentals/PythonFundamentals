from math import pi


def rec(a, b):
    """area of a rectangle"""
    r = a * b
    return r

def tri(h, s):
    """area of a triangle"""
    t = 1/2 * h * s
    return t

def cir(r, pi):
    """area of a circle"""
    c = pi * r**2
    return float(round(c, 2))

user = None

while user != "rectangle" or "triangle" or "circle" or "exit": 

    user = input("What area are we calculating: rectangle, triangle or circle? Or exit.\n")
    
    if user == "rectangle":
        a = int(input("Enter side a = "))
        b = int(input("Enter side b = "))
        print(f"Area of rectangle with side {a} and {b}:", rec(a, b))
     

    elif user == "triangle":
        h = int(input("Enter height h = "))
        s = int(input("Enter base s = "))
        print(f"Area of triangle with height {h} and base {s}:", tri(h, s))
        

    elif user == "circle":
        r = int(input("PI we have, enter only circle radius r = "))
        print(f"Area of circle with radius {r}:", cir(r, pi))
       
    elif user == "exit":
        break   
       
    else:
        print("Error, use only rectangle, triangle or circle. Or exit.")