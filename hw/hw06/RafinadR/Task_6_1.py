k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = []
m = []
n = []

for i in range(len(k)):

    if (k[i] % 2 == 0):
        l.append(k[i])

    elif (k[i] % 3 == 0):
        m.append(k[i])

    else:
        n.append(k[i])

print("Our numbers:", k[:])
print("Numbers that are divisible by 2:", l[:])
print("Numbers that are divisible by 3:", m[:])
print("Numbers that are not divisible by 2 and 3:", n[:])