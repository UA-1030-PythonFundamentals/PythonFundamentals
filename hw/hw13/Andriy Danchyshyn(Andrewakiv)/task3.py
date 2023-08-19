def func1(arr):
    lst = []
    for i in arr:
        lst.append(int(i))
    return lst


def func2(arr):
    return list(map(lambda i: int(i), arr))


print(func1(['1', '2', '3', '4', '5', '7']))
print(func2(['1', '2', '3', '4', '5', '7']))
