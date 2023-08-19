from functools import reduce


def func(arr):
    return reduce(lambda i, j: i if i > j else j, arr)


print(func([5, 1, 3, 7, 9, 4]))
