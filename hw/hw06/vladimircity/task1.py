# Task1. In the range from 1 to 10 determine
# • even numbers that are divisible by 2,
# odd numbers, which are divisible by 3,
# numbers that are not divisible by 2 and 3.
divisible_by_2 = []
divisible_by_3 = []
not_divisible_by_2_3 = []

for i in range(1, 11):
    if not i%2:
        divisible_by_2.append(i)
    elif not i%3:
        divisible_by_3.append(i)
    else:
        not_divisible_by_2_3.append(i)

print('divisible by 2:', divisible_by_2)
print('divisible by 3:', divisible_by_3)
print('not divisible by 2 and 3:', not_divisible_by_2_3)