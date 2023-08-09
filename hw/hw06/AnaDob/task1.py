even_by_2 = []
odd_by_3 = []
not_divisible_by_2_and_3 = []
for number in range(1, 11):
    if number%2 == 0:
        even_by_2.append(number)
    elif number%3 == 0:
        odd_by_3.append(number)
    elif number%2!=0 and number%3!=0:
        not_divisible_by_2_and_3.append(number)

print("Even numbers divisible by 2 are:", even_by_2)
print("Odd numbers divisible by 3 are:", odd_by_3)
print("Numbers not divisible by 2 and 3 are:", not_divisible_by_2_and_3)
