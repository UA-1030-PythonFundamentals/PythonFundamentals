my_list = list(range(1, 11))

even_divisible_2 = my_list[1::2]
odd_divisible_3 = [elem for elem in my_list if elem % 2 != 0 and not elem % 3]
not_divisible_2_3 = [elem for elem in my_list if elem % 2 != 0 and elem % 3 != 0]
result = f"Even numbers that are divisible by 2: {even_divisible_2}\n" \
         f"Odd numbers, which are divisible by 3: {odd_divisible_3}\n" \
         f"Numbers that are not divisible by 2 and 3 : {not_divisible_2_3}"

print(result)
