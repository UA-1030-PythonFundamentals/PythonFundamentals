##Using several decorators, create a sandwich consisting of
##lettuce, tomatoes and meat.
##<\ ^^^^^^^ />
### tomato #
##– meat–
##~ salad ~
##<\ ______ /> --HW13--Aug 14,2023--PT26

def meat(fn):       #Decorator 1

    fn()
    print("...Meat...")
    return fn

def sal(fn):        #Decorator 2

    fn()
    print("...Salad...")
    return fn
print(70*"*")

def tom(fn):        #Decorator 3

    fn()
    print("...Tomatoes...")
    return
print(70*"*")    


@tom
@sal
@meat
def menu():
    print("...Sandwich consists of :")
    return
print(70*"*")
