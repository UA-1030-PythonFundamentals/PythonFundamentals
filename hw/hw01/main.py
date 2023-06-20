A = float(input("First number: "))                
B = float(input("Second number: "))
operation = input("Operation (+, -, *, /, **, //, %): ")
result = None

if operation == "+":
    result = (A + B)
    print(result)
elif operation == "-":
    result = (A - B)
    print(result)
elif operation == "*":
    result = (A * B)
    print(result)
elif operation == "/":
    result = (A / B)
    print(result)
elif operation == "**":
    result = (A ** B)
    print(result)
elif operation == "//":
    result = (A // B)
    print(result)
elif operation == "%":
    result = (A % B)
    print(result)
else:
    print("Choose another operation")