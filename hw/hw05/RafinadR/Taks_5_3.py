n = int(input("Enter number:\n"))
f = 1

while n > 0:
    f = f * n
    n = n - 1
    
print("Factorial of the number is: ", f)