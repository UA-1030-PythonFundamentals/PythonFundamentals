#Fibonacci
num = int(input("Enter the number: "))
current = 1
previous = 0
print("Sequence of Fibonacci numbers:", end=" ")
while previous <= num:
    print(previous, end=" ")
    previous, current = current, previous + current