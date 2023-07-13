def clac(string):
    dct = {}
    for i in string:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    return dct


print(clac('hello'))
