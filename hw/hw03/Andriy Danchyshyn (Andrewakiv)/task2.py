num = 5274

# task1
product = 1
for i in str(num):
    product *= int(i)
print(product)

# task2
reverse = str(num)[::-1]
print(reverse)

# task3
print(''.join(sorted(str(num))))

