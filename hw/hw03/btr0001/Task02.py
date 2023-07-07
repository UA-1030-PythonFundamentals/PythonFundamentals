import math

num = int(input("Enter four-digit natural number:"))
num_str = str(num)

lst = [int(num_str[0]), int(num_str[1]), int(num_str[2]), int(num_str[3])]

print(lst)

res = math.prod(lst)

print(f"Result of production = {res}")

print(f"Sorted numbers: {sorted(lst)}")