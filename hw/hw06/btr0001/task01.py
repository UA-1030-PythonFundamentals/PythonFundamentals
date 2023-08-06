even_numbers = []
odd_numbers = []
not_divisible_numbers = []
not_divisible_numbers2 = []

for n in range(1, 11):
    if n % 2 == 0:
        even_numbers.append(n)
    if n % 2 == 1 and n % 3 == 0:
        odd_numbers.append(n)
    if not(n % 2 == 0 or n % 3 == 0):
        not_divisible_numbers.append(n)
    if not(n % 2 == 0 and n % 3 == 0):
        not_divisible_numbers2.append(n)

print(even_numbers)
print(odd_numbers)
print(not_divisible_numbers)
print(not_divisible_numbers2)