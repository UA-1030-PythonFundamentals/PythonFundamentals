# list
# dict
# set
#
# tuple
#
# l = [i for i in range(10)]
# print(l)
# l = {i for i in range(10)}
# print(l)
# l = {i:i**i for i in range(10)}
# print(l)
# l = (i for i in range(4))
# print(l)
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
# l = [(i, j, k) for i in range(5) for j in range(i) for k in range(j)]
# print(l)
# l = []

# for i in range(5):
#     for j in range(i):
#         for k in range(j):
#             l.append((i, j, k))
# for i in range(5):
#     print(f"i:{i}")
#     for j in range(i):
#         print(f"\tj:{j}")
#         for k in range(j):
#             print(f"\t\tk:{k}")
#             l.append((i, j, k))
# print(l)
#
# vec1 = [3, 10, 2]
# vec2 = [-20, 5, 1]
# z = zip(vec1, vec2)
# print(list(z))
# dot_mul = [u*v for u, v in zip(vec1, vec2)]
# print(dot_mul)
# vec1 = [3, 10, 2, 1]
# vec2 = [-20, 5, 1]
# vec3 = [-21, 51, 11, 11, 21]
#
# z = zip(vec1, vec2, vec3)
# print(list(z))
# print(z)

# winning_lottery_numbers = [0, 4, 3, 2, 3, 1]
#
# m = map(lambda x: x**3, winning_lottery_numbers)
# print(winning_lottery_numbers)
# print(m)
# print(list(m))
# def my_generator():
#     print("Inside my generator")
#     yield 'a'
#     yield 'b'
#     yield 'c'
# g1 = my_generator()
#
# print(f"{next(g1)=}")
# g2 = my_generator()
# print(f"{next(g2)=}")
# print(f"{next(g1)=}")
# print(f"{next(g1)=}")
# print(f"{next(g2)=}")
# for i in my_generator():
#     print(i)
#
# print(f"{next(g1)=}")

# def my_generator_int(n):
#     count = 0
#     while True:
#         print("before yield ",count)
#         yield count
#         count += 1
#         print("after yield ", count)
#         if count > n:
#             break
#
# g = my_generator_int(5)
# print(g)
# print(list(g))
#
# print(f"{next(g)=}")
# print()
# print(f"{next(g)=}")
# print()
# print(f"{next(g)=}")
# print()
# print(f"{next(g)=}")
# print()
# print(f"{next(g)=}")
# print()
# print(f"{next(g)=}")
# print()
# print(f"{next(g)=}")
# print()
# n = 10
# for i in range(5):
#     l = list(range(n))
#     g = my_generator_int(n)
#     print(f"{n=} l:", l.__sizeof__(), "g:", g.__sizeof__() )
#     n *= 10
#
# import time
# start = time.time()
# l = []
# for i in range(20000):
#     l.append(i)
# end = time.time()
# print(end-start)
# start = time.time()
# l = [i for i in range(20000)]
# end = time.time()
# print(end-start)

# def my_f(element):
#     print(type(element), element)
#     return element
#
# my_f(1)
# my_f("1")
# my_f(lambda x:x)
#
# @my_f
# def sum_ab(a,b):
#     return a,b
#
# sum_ab(1,2)
# sum_ab(1,2)
# sum_ab(1,2)


def run_time(func):
    import time
    def wraper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{end-start}\t{func.__name__} {args} {kwargs} \t=> {result}")
        return result
    return wraper
def star(func):
    print(f"{id(func)=}")

    def inner(*args, **kwargs):
        print("*" * 30)
        result = func(*args, **kwargs)
        print("*" * 30)
        return result

    print(f"{id(inner)=}")
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        result = func(*args, **kwargs)
        print("%" * 30)
        return result

    return inner


# @star
# @percent
# @percent
@run_time
@star
def sum_ab(a, b):
    return a, b

@run_time
@star
def sum_abc(a, b, c):
    return a, b,c


print(f"{id(sum_ab)=}")
print(f"{id(sum_abc)=}")
print(sum_ab(1, 2))
print(sum_ab(1, 20))
print(sum_abc(1, 200, 33))



def foo_line(symbol):
    def decorator(func):
        def inner(*args, **kwargs):
            print(symbol*30)
            result = func(*args, **kwargs)
            print(symbol * 30)
            return result
        return inner
    return decorator
@foo_line("<>")
def sum_abc(a, b, c):
    return a, b,c

sum_abc(1,2,3)
@foo_line("\/")
def sum_abc(a, b, c):
    return a, b,c
sum_abc(1,2,3)
