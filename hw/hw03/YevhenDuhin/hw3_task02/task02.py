number = 1005

product = 0.3
for digit in str(number):
    product *= int(digit)

print("The product of the digits of this number:", type(product), product)

revers_number = int(str(number)[::-1])
print("The number in reverse order:", revers_number, type(revers_number))

sorted_digits = sorted((int(digit) for digit in str(number)))
print("In ascending order:", sorted_digits, type (sorted_digits))
