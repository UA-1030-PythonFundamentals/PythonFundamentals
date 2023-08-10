def age(a):
    try:    
        a = int(a)
        if a < 0:
            raise ValueError(f"That {a} is not a positive number")
        if a == 0:
            raise ValueError(f"Only {a}? You are just newborn :)")
        if a % 2 == 0:
            print(f"Your age {a} is even number")
        else:
            print(f"Your age {a} is odd number")
        
    except ValueError as v:
        print(v)          
    except TypeError as t:
        print(t)

age(input("Enter your age: "))