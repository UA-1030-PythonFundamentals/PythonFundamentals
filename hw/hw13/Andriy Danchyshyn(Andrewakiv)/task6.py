def func(start, stop, step=1):
    cur = start
    while cur < stop:
        yield cur
        cur += step


for num in func(1, 10, 3):
    print(num)
