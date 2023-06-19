#task2 
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
calculation = f"""
A + B = {first + second}
A - B = {first - second}
A * B = {first * second}
A / B = {first / second}
A ** B = {first ** second}
A // B = {first // second}
A % B = {first % second}
"""
print(calculation)