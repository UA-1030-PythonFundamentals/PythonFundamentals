arr = list(range(1, 11))
even = arr[1::2]
print('even: ', even)
odd = [i for i in arr if i % 3 == 0 and i % 2 != 0]
print('odd: ', odd)
n2n3 = [i for i in arr if i % 3 != 0 and i % 2 != 0]
print('numbers that are not divisible by 2 and 3: ', n2n3)
