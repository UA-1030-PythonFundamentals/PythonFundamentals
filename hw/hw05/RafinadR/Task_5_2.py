n = int(input("n = "))

f1 = 0
f2 = 1
f3 = 0
print(f1)
while f3 < n:
                       
        f3 = f1 + f2
        f1 = f2
        f2 = f3

        print(f1)
