def combinations(list1, list2):
    for i in list1:
        for j in list2:
            yield (i, j)