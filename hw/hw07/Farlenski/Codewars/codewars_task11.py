def count_sheeps(sheep):
    return sheep.count(True)


lst = [True, True, True, False,
       True, True, True, True,
       True, False, True, False,
       True, False, False, True,
       True, True, True, True,
       False, False, True, True]
print(count_sheeps(lst))
