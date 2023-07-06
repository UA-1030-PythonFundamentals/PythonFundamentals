n = int(input('Enter number:'))
fact = 1


for num in range(n + 1):
    if num==0:
        print(fact)
    else:
        fact *= num
        print(fact)
