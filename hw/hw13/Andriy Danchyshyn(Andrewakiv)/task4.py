def convert(mile):
    return mile*1.6


def func(arr):
    return list(map(convert, arr))


def func1(arr):
    return list(map(lambda mile: mile*1.6, arr))


print(func([1, 4, 6, 8, 90]))
print(func1([1, 4, 6, 8, 90]))
