#HW5 PT8 , Fibonacci numbers - June  28, 2023
print(70*"*")
n = int(input("Enter arbitrary integer number : "))
print()

n1 = 0
n2 = 1
f = 0
i = 1

print("Here is your Fibonacci numbers series :")  
while i <= n:
    print(f, end=" ")
    i += 1
    n1 = n2
    n2 = f
    f = n1 + n2

print()   
print(70*"*")
