a = input("Enter first: \n")
b = input("Enter second: \n")

print("You enter a = ", a)
print("You enter b = ", b)

(a, b) = (b, a)

print("After interchange a =", a, "\nAfter interchange b =", b)