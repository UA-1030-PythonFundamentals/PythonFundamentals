# Counting sheep...

sheep = [
    True, True, True, False,
    True, True, True, True,
    True, False, True, False,
    True, False, False, True,
    True, True, True, True,
    False, False, True, True
]


def count_sheeps(sheep):
    return sum([x for x in sheep if x])


print(count_sheeps(sheep))
