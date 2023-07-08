# Product of the digits
number = 2134
product = 1
for n in str(number):
	product *= int(n)
    
print(f'The product of all the digits in {number} equals {product}')

# Write the number in reverse order
print()
print(str(number)[::-1])

# Sort digits ascending
print()
print(*sorted([*str(number)]))