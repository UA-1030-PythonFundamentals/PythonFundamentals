divisible_by_2 = [];
divisible_by_3 = [];
not_divisible_by_2_and_3 = [];

for i in range(1, 11):
    if i % 2 == 0:
        divisible_by_2.append(i)
    elif i % 3 == 0:
        divisible_by_3.append(i)
    else:
        not_divisible_by_2_and_3.append(i)

print(f"Even numbers that are divisible by 2: {divisible_by_2}")
print(f"Odd numbers that are divisible by 3: {divisible_by_3}")
print(f"Numbers that are not divisible by 2 and 3: {not_divisible_by_2_and_3}")

