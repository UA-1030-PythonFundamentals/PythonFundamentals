#Factorial
num = int(input("Enter the number: "))
result = 1

for i in range(1, num+1):
    if num == 0: 
        result = 1
    else: 
        result *= i

print(f"Factorial is {result}")