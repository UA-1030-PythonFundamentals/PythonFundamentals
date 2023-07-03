listOne = []
listTwo = []
listThree = []

for i in range(1, 11):
    if i % 2 == 0:
        listOne.append(i)
print(listOne)

for i in range(1, 11):
    if i % 3 == 0:
        listTwo.append(i)
print(listTwo)

for i in range(1, 11):
    if i % 2 != 0 and i % 3 != 0:
        listThree.append(i)
print(listThree)