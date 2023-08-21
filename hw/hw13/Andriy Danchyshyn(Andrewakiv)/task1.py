def func(arr):
    return list(map(lambda name: hash(name), arr))


print(func(['Sam', 'Don', 'Daniel']))
