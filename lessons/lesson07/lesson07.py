# # def print_name():
# #     """
# #     this is function
# #     :return:
# #     """
# #     print("name", end="->")
# #     print("Vasyl")
# #
# #
# # print(print_name)
# # print_name()
# # print_name()
# # print_name()
# # p = print_name
# # print(p)
# # p()
# # print_name()
# # print(print_name.__doc__)
# # help(print_name)
# # print_name()
# # # sum()
# # print(sum.__doc__)
# # help(sum)
# # print(print_name())
# # r = print_name()
# # print(r)
#
# # def my_f(n):
# #     if n > 0:
# #         return n
# #     else:
# #         return n ** 2
# #
# #
# # result = my_f(5)
# # print(result)
# # result = my_f(-5)
# # print(result)
# # result = my_f(0)
# # print(result)
#
# # def my_f(n):
# #     if n == 0:
# #         return "Zero"
# #     else:
# #         if n > 0:
# #             return n
# #     return n ** 2
# #
# #
# # result = my_f(5)
# # print(result)
# # result = my_f(-5)
# # print(result)
# # result = my_f(0)
# # print(result)
#
# # def my_f(n):
# #     """
# #     function return True if n in [0, 9] else None
# #     :param n: int
# #     :return: True or None
# #     """
# #     for i in range(10):
# #         if n == i:
# #             return True
# #     return  # return None
# #
# #
# #
# # result = my_f(5)
# # print(result)
# # result = my_f(-5)
# # print(result)
# # result = my_f(0)
# # print(result)
# #
# # def my_f(name):
# #     return f"my name is: {name}"
# #
# #
# # print(my_f("Liubomyr"))
#
#
# # my_f()
# # my_f("test", 2)
# # def my_f(name, age):
# #     result = (f"my name is: {name}"
# #               f"i am {age} years old")
# #     return result
# #
# #
# # print(my_f("Liubomyr", 37))
# # # print(my_f("Liubomyr"))
#
#
# # def my_f(name, age=18):
# #     result = (f"my name is: {name}"
# #               f"i am {age} years old")
# #     return result
# #
# #
# # print(my_f("Liubomyr", 37))
# # print(my_f("Ivan"))
# # print("a", "b" ,'c', end="||||", sep="-")
#
# # my_f(12, 12 ,12)
# # def my_f2(a, b, c=1, d=100):
# #     result = d * (a + b) ** c
# #     print(f"{a=} {b=} {c=} {d=}\td*(a+b)**c=>{d}*({a}+{b})**{c}={result}")
# #     return result
# #
# #
# # my_f2(1, 2)
# # my_f2(3, 2, 9)
# # my_f2(4, 5, 7, 13)
# # # my_f2(4, 5, 7, 13, 99)#error
# # my_f2(d=10, c=15, a=99, b=77)
# # my_f2(10, c=15, d=99, b=77)
# # # my_f2(10, c=15, a=99, b=77) #error
# # # my_f2(10, c=15, d=99, 77)  # error
# # my_f2(10, 77, c=15, d=99)
#
#
# # def my_f(a, *args, b=1, **kwargs):
# #     print(f"{a=} {args=} {b=} {kwargs=}")
# #
# #
# # my_f(1)
# # my_f(1, 2)
# # my_f(1, 2, 3)
# # my_f(1, 2, 3, 4)
# # my_f(1, 2, 3, 4, b=12)
# # my_f(1, 2, 3, 4, b=12, c=1)
# # # my_f(1, 2, 3, 4, b=12, 1) #error
# # my_f(1, 2, 3, 4, b=12, c=1, d=15)
# #
# # l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# # my_f(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], )
# # my_f(*l)
# # # my_f(**l) #error
# # d = {
# #     "a": 1,
# #     "b": "str",
# #     "c": "test",
# #     "f": None
# # }
# # my_f(*d)
# # my_f(*(d.keys()))
# # my_f(**d)
# # my_f(a=d["a"], b=d["b"], c=d["c"], f=d["f"])
#
# # def FaFa():
# #     print("dd")
# #
# # FaFa()
#
# # def avarage(*args):
# #     result = sum(args) / len(args)
# #     return result
# #
# #
# # print(avarage(1, 2, 3, 4, 5))
# #
# # from statistics import mean
# #
# #
# # def func(*args):
# #     return mean(args)
# #
# #
# # print(func(1, 2, 3, 4, 5))
# # a = 1
# # print(dir())
# #
# #
# # def my_f():
# #     b = 10
# #     print(dir())
# #
# #
# # my_f()
# # # print(b)#error
# #
# #
# # def my_f_a():
# #     a = 10
# #     print(a)
# #
# #
# # print(a)
# # my_f_a()
# # print(a)
#
# # a = 1
# # def prirint_a():
# #     print(a)
# #     a = 10
# #
# # prirint_a()
#
# # a = [12]
# # def prirint_a():
# #     print(a)
# #     a.append(15)
# #     print(a)
# # prirint_a()
# # print(a)
# #
# # def prirint_a():
# #
# #     a = []
# #     a.append(15)
# #     print(a)
# # prirint_a()
# # print(a)
#
# # a = 1
# #
# #
# # def prirint_a():
# #     global a
# #     print(a)
# #     a = 20
# #     print(a)
# #
# # prirint_a()
# # print(a)
# #
# # def funck(n):
# #     x = "local"
# #     def inner():
# #         x = "nonlocal"
# #         print(x)
# #     inner()
# #     print(x)
# #
# # funck(5)
# # def funck(n):
# #     x = "local"
# #     def inner():
# #         nonlocal x
# #         x = "nonlocal"
# #         print(x)
# #     inner()
# #     print(x)
# #
# # funck(5)
# # # print(x)# error
# #
# # def funck(n):
# #     x = "local"
# #     def inner():
# #         global x
# #         x = "nonlocal"
# #         print(x)
# #     inner()
# #     print(x)
# #
# # funck(5)
# # print(x)
#
# #
# # def get_sum_func():
# #     all_sum = 0
# #     def innet(*args):
# #         nonlocal all_sum
# #         all_sum += sum(args)
# #         return all_sum
# #     return innet
#
#
# #
# # my_s = get_sum_func()
# # print(my_s(1,2,3))
# # print(my_s(1,2,4))
# # print(my_s(1))
# # print(my_s(222,3,4))
# #
# # def fuc(n):
# #     result = 1
# #     for i in range(1, n+1):
# #         result *= i
# #     return result
# #
# # print(fuc(10))
# # print(fuc(8))
# #
# # def fuc(n):
# #     if n in (0, 1):
# #         return 1
# #     else:
# #         print(f"{n}*(f({n-1}))")
# #         return n*fuc(n-1)
# #
# # print(fuc(10))
# # print(fuc(8))
#
# # my_f = lambda a, b: a ** b
# #
# # print(my_f(1.5, 5))
# #
# #
# # def my_f(a, b):
# #     return a ** b
# #
# #
# # l = [1, "12", "33", 7]
# # l.sort(key=lambda e: int(e))
# # print(l)
# #
# #
# # def l_s(e):
# #     return int(e)
# #
# #
# # l = [1, "12", "33", 7]
# # l.sort(key=l_s)
# # print(l)
#
#
# git pull origin main
#
#
# # git pull origin/main
# print(dir(list))


l = [1,2,4]
# l.append(1,2)
# list.append(l, 1,2)
