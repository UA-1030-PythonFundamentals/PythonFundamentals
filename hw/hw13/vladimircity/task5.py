def fibonacci_numbers():
    first = 0
    second = 1
    yield first
    yield second
    while True:
        next = first + second
        first, second = second, next
        yield next


fib = fibonacci_numbers()

for i in range(10):
    print(next(fib))
