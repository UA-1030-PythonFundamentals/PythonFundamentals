def max_of_two_numbers(num1, num2):
    return max(num1, num2)

number1 = float(input("Enter first num: "))
number2 = float(input("Enter second num: "))

max_number = max_of_two_numbers(number1, number2)
print("Larger number:", max_number)
