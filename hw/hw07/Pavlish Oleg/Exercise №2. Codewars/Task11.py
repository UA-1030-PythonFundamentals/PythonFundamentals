def count_sheeps(sheep):
    return sheep.count(True)
array1 = [True,  True,  True,  False,
                  True,  True,  True,  True ,
                  True,  False, True,  False,
                  True,  False, False, True ,
                  True,  True,  True,  True ,
                  False, False, True,  True ]
print(count_sheeps(array1))
