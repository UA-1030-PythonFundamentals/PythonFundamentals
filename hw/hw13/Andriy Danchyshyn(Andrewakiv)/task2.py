def func(arr):
    return list(filter(lambda col: col == 'red', arr))


print(func(["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]))
