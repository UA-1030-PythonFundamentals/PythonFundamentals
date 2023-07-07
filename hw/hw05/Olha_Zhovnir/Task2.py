n = int(input("Enter the n value: "))

a=0
b=1

if n>2:
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)



