# i = 1
# while i < 5:
#     print(i)
#     i += 2
# from time import sleep
# while True:
#     print("test")
#     sleep(3)

#
# for i in range(5):
#     print(i)
# for element in ["test", 15, {"d": 10}]:
#     print(element)

# l = ["test", 15, {"d": 10}]
# for element in l:
#     print(element)
# for i in range(len(l)):
#     print(l[i])
# for i in "range(len(l))":
#     print(i)
# for i in {1, 2, 3, "a"}:
#     print(i)

# print(range(5))
# print(list(range(5)))
# print(list(range(-5)))
# print(list(range(-5, 5)))
# print(list(range(-5, 5, 3)))


# s = "testmy"
# s = "tes"
# print(list(enumerate(s)))
# for e in enumerate(s):
#     print(e , e[0], e[1])
# i, j = (0, 't')
# print(i, j)
# for i, value in enumerate(s):
#     print(i, value)
#
# d = {"a": 12,
#      "b": 5,
#      7: "z"}
#
# for i in d:
#     print(i, d[i])
# print(d.items())
#
# for key, value in d.items():
#     print(key, value)
# print(list(enumerate(d)))
#
#
# def my_enumerate(cont):
#     result = []
#     i = 0
#     for element in cont:
#         result.append((i, element))
#         i += 1
#     return result
#
#
# print(my_enumerate(d))
#
#
# for i in range(10):
#     if i > 3:
#         break
#     print(i)

# i = 0
# while i < 10:
#     if i > 3:
#         break
#     print(i)
#     i += 1
#
# i = 0
# while i < 10:
#     # if i > 3:
#     #     break
#     print(i)
#     i += 1
# else:
#     print("else", i)
# print("end")
# i = 0
# while i < 10:
#     i += 1
#     if i % 2:
#         continue
#     print(i)
# else:
#     print("else", i)
# print("end")
#
# for i in range(5):
#     pass
# task 1
# print("Task1 - 1")
# for i in range(100):
#     if i % 2 == 0:
#         print(i)
# print("Task1 - 1")
# for i in range(100):
#     if not i % 2:
#         print(i)
# for k in range(1,100,2):
#     print(k)
# i = 0
# while i < 100:
#     i += 1
#     if i % 2 == 0:
#         print(i)
# print("Task1 - 2")
# i = 0
# while i < 100:
#     if i % 2 == 0:
#         print(i)
#     i += 1
#
# task 2
# print("Task2 - 1")
# for i in range(100):
#     if i % 2 == 0:
#         continue
#     print(i)
# print("Task2 - 2")
# for i in range(100):
#     if i % 2 == 1:
#         print(i)
#
# print("Task2 - 3")
i = 1
# while i < 100:
#
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)


# print("Task2 - 4")
# i = 0
# while i < 100:
#     if i % 2 == 1:
#         print(i)
#     i += 1

# print("jon" > "jona")
# print("a" > "a")
# print("aa" > "ab")
# print("ab" > "b")
# # for i in range(256):
# #     print(f"{i} - {chr(i)}")
# "bvdhsbfk".count("is")
# "bvdhsbfk".count("is", 4)
# "bvdhsbfk".count("is", 4, 15)
# x = 5
# y = 10
# print(x and y)
# z = []
# print(x and z and y)

# import random
#
#
# def false(i=""):
#     result = random.choice([0, False, None, [], (), set{}, dict{}])
#     print(f"{i}-false", result)
#     return result
#
#
# def true(i=""):
#     result = random.choice([1, True, [1], "a"])
#     print(f"{i}-true", result)
#     return result
#
#
# # print("e1", true() and true() and true() and true())
# # print("e2", true() and true() and false() and true())
# # print("e3", false() or false() or false() or false())
# # print("e3", false(1) or true(2) or false(3) or false(4))
# # print("e3", false(1) or true(2) or false(3) or false(4))
# print("e3", false(1) or true(2) and false(3) or false(4))
# print("e3", false(1) or true(2) and true(3) or false(4))

for i in range(300):
    t = i + 1
    t = t - 1
    print(i, t, id(i) == id(t))
print(2 ** 8)


def divisible_by_five(number):
    result = number % 5 == 0
    return result


print(True == divisible_by_five(5))
print(False == divisible_by_five(121))
print(True == divisible_by_five(505))

number = 5
result = number % 5 == 0
print(result)

number = 121
result = number % 5 == 0
print(result)

number = 505
result = number % 5 == 0
print(result)
