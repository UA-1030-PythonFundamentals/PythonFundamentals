# Task_13_1
names = ["Sam", "Don", "Daniel"]
h_names = list(map(lambda i: hash(i), names))
print(f"\nTask_13_1:\nhash for{names}:\n", h_names)


# Task_13_2
l = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]
def red(r):
    if r == "red":
        return r
l_red_1 = list(filter(lambda i: red(i), l))
l_red_2 = list(filter(lambda i: i == "red", l)) 
print(f"\nTask_13_2:\nfilter 'red' for {l}:\n{l_red_1}\n{l_red_2}")


# Task_13_3
l = ['1', '2', '3', '4', '5', '7']
int_l = []
for i in range(len(l)):
    int_l.append(int(l[i]))
print("\nTask_13_3(1):\n",int_l, f"is int type of {l}")
int_l = list(map(int, l))
print("Taks_13_3(2):\n",int_l, f"is int type of {l}")


# Task_13_4
print("\nTask_13_4")
print("Convert miles to kilometers\n")
miles = [100, 200, 300, 400]
def mile_to_km(m):
    k = m * 1.6
    return k
kilometers = list(map(mile_to_km, miles))
print("miles:", miles)
print("kilometers:", kilometers)
for e in range(len(miles)):
    print(f"{miles[e]} miles = {kilometers[e]} km")

kilometers = list(map(lambda m: m*1.6, miles))
print("second convert is same: km:", kilometers)


# Task_13_5
from functools import reduce
l = [23, 4, 45, 2, 6, 156, 20]
max_l = reduce(lambda a, b: a if (a>b) else b, l)
print("\nTask_13_5:\n",max_l, f"is biggest number in {l}")


# Task_13_6
def distance(city_a, city_b, speed):
    global c
    c = 0
    car_pocition = city_a
    while car_pocition < city_b:
        yield car_pocition
        car_pocition += speed
        c += 1

print("\nTask 13_6:")
print("Simple generator function similar to the range iterator\n")

for i in distance(0, 560, 90):
    print(i, f"km for {c}h driving")


#Task_13_7
def top(func):
    def inner(*args, **kwargs):
        print("<\ ^^^^^^^ />")
        func(*args, **kwargs)
    return inner

def tomato(func):
    def inner(*args, **kwargs):
        print("  # tomato #")
        func(*args, **kwargs)
    return inner

def meat(func):
    def inner(*args, **kwargs):
        print("    –meat–")
        func(*args, **kwargs)
    return inner

def salad(func):
    def inner(*args, **kwargs):
        print("    ~salad~")
        func(*args, **kwargs)
    return inner

def bottom(func):
    def inner(*args, **kwargs):
        print("  <\ ______ />")
        func(*args, **kwargs)
    return inner
@top
@tomato
@meat
@salad
@bottom
def sandwich():
    print("it's my sandwich")
print("\nTask_13_7:\n")
sandwich()
