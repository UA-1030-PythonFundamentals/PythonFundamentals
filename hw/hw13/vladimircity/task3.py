def combinations(list1, list2):
    for i in list1:
        for j in list2:
            yield (i, j)


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for combination in combinations(list1, list2):
    print(combination)