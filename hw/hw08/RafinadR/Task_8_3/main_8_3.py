import support_8_3 as area

user = None

while user != "rectangle" or "triangle" or "circle" or "exit": 

    user = input("What area are we calculating: rectangle, triangle or circle? Or exit.\n")
    
    if user == "rectangle":
        a = int(input("Enter side a = "))
        b = int(input("Enter side b = "))
        print(f"Area of rectangle with side {a} and {b}:", area.rec(a, b))

    elif user == "triangle":
        h = int(input("Enter height h = "))
        a = int(input("Enter base a = "))
        print(f"Area of triangle with height {h} and base {a}:", area.tri(h, a))
        
    elif user == "circle":
        r = int(input("PI we have, enter only circle radius r = "))
        print(f"Area of circle with radius {r}:", area.cir(r))
       
    elif user == "exit":
        break   
       
    else:
        print("Error, use only rectangle, triangle or circle. Or exit.")