import random
list = []
for k in range(10):
    list.append(random.randint(1, 10))
print("Список:", list)
list_2 = []
list_3 = []
list_23 = []
for i in range(len(list)):
    if (list[i] % 2 == 0):
        list_2.append(list[i])
    if (list[i] % 3 == 0):
        list_3.append(list[i])
    elif (list[i] % 2 and 3 != 0):
        list_23.append(list[i])
print("Список чисел, що діляться на 2:", list_2)
print("Список чисел, що діляться на 3:", list_3)
print("Список чисел, що не діляться на 2 і 3:", list_23)


