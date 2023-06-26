# # i = 1
# # l = []
# # print(id(i))
# # print(id(l))
# # i += 1
# # l.append(1)
# # print(id(i))
# # print(id(l))
# #
# # for i in range(1100, 1110):
# #     i = i+1
# #     l.append(i)
# #
# # a = 1
# # print(a, type(a), type(a) is int)
# # print(a, type(a), type(a) is str)
# # a = "1aaaa"
# # print(a, type(a), type(a) is str)
# # a = True
# # print(type(a), type(a) is bool)
# #
# #
# # class T1:
# #     pass
# #
# #
# # class T2(T1):
# #     pass
# #
# #
# # t1 = T1()
# # t2 = T2()
# # print(type(t1) is T1, type(t1))
# # print(isinstance(t1, T1))
# # print(type(t2) is T1, type(t2))
# # print(isinstance(t2, T1))
# # print(isinstance(t2, int))
# # a = 1 + 2 + \
# #     3 + 4
# # print(a)
# # a = (1 + 2 +
# #      3 + 4)
# # print(a)
# # a = [1 + 2 +
# #      3 + 4]
# # print(a)
# #
# # a, b, c = 1, 2, 3
# # print(a, b, c)
# #
# # l = [5, 7, 9]
# # a, b, c = l
# # print(a, b, c)
# # PI = 3.14
#
#
# # a = 100
# # print(a)
# # a = 0b100
# # print(a)
# # a = 0o100
# # print(a)
# # a = 0x100
# # print(a)
# #
# # a = 100_00_0_0
# # print(a)
# # a = 97_04_36_518
# # print(a)
# # # a = 97 04 36 518 # error
# # print(a)
# #
# #
# #
# # a = 100.0
# # print(a)
# # a = 100.
# # print(a)
# # a = .0
# # print(a)
# # a = 15e3
# # print(a)
# # a = 15*10**3
# # print(a)
# # a = 15e-3
# # print(a)
# # a = 15*10**(-3)
# # print(a)
#
# #
# # a = True
# # print(a)
# # a = False
# # print(a)
#
# # a = None # null
# l = [1, 2, 3, 4, "a"]
# print(l[3])
# d = {"key1": "value",
#      2: 15161}
# # print(d[3]) # error
# print(d["key1"])
# # print(d[2])
#
# a = int("12")
# print(a)
# a = int("100", 2)
# print(a)
# a = int("100Z", 36)
# print(a)
# a = int("9", 36)
# print(a)
# a = int("a", 36)
# print(a)
# a = int("z", 36)
# print(a)
# a = int("10", 36)
# # print(a)
# a = float("3.5")
# print(a)
# a = float(3)
# print(a)
import decimal

# a = 10**4299
# print(a)
# import sys
# print(sys.set_int_max_str_digits(9000))
# a = 10**8999
# print(a)

# print(str(99))
#
# for i in range(255):
#     print(i, chr(i), sep=" -> ")
#
# s = "bsdjhkbv fbd8416Y^*&Yb9u"
# for i in s:
#     print(i, ord(i), sep=" -> ")
# a = 19
#
# print(bin(a))
# print(oct(a))
# print(hex(a))

# print(int(10.1))
# print(int(10.9))
# print(round(10.1))
# print(round(10.9))
# print(round(10.98745, 2))
#
# s = "test text"
# print(s[1])
# print(s[1:5])
# print(s[0:3])
# print(s[:3])
# print(s[3:])
# print(s[:])
# print(s[2:9:3])
# print(s[-1])
# print(s[-3])
# print(s[2:-2])
# print(s[::-1])
# print(1 + 1.)
# print(1. + 1)

# "test"
# 'test'
# """te
# st"""
# '''te
# st'''
# s = "test"
# # s[2] = "3"
# s = s[:2] + "3" + s[3:]
# print(s)


# s = "test\ntest"
# print(s)
# s = "test\ntest\txx"
# print(s)
# s = "test\"s"
# print(s)


# template = "my name is %s, age %d"
# print(template)
# print(template % ("Liubomyr", 37))
# print(template % (25, 37))
# # print(template % (25, "vsdgf"))
# template = "my name is {}, age {}"
# print(template.format("Liubomyr", 37))
# template = "my name is {name}, age {age}"
# print(template.format(age=37, name="Liubomyr"))
# template = "my name is {0}, age {1}! {0}"
# print(template.format("Liubomyr", 37))
#
# name = "Liubomyr"
# def get_age():
#     age = input("age:")
#     return int(age)
# print(f"my name is {name}, age {get_age()}! {template}")

# print(dir(str))
#
# s = "my name Liumomyr. age 25."
# print([method for method in dir(str) if not method.startswith("_")])
# print(s.capitalize())
# print(s.center(100))
# print(s.center(1))
# print(s.endswith("25"), s.endswith("25."))
# print(s.find("age"), s.find("m", 3))
# print(s.find("aage"))
# print(s.index("age"))
# # print(s.index("aage")) # error
# print("as12".isalnum())
# print("as12!".isalnum())
# print("as12!".lower())
# print("as12!".upper())
# print("as121!".replace("1", "99"))
#
# print("asd, sbbhdjv, jasdbvi, ahdsbv".split())
# print("asd, sbbhdjv, jasdbvi, ahdsbv".split("as"))
# print("==".join(['', 'd, sbbhdjv, j', 'dbvi, ahdsbv']))
# print("   test ttt   ".strip())
# print("   test ttt   ".zfill(20))
# print("   test ttt   ".zfill(10))

print(round(4.5))
print(round(4.51))
print(round(4.5))
print(round(5.5))
print(round(6.5))
print(0.3+0.3+0.3)

# decimal.Rounded