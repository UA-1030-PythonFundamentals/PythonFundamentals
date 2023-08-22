def fibonacci_numbers():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci_numbers()