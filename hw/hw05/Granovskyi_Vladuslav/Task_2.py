n = int(input())
def fib(n):
    a = 0
    b = 1
    print(a, b)
    for i in range(2, n+1):
        c = a + b
        a, b = b, c
        print(c)
print(fib(n))
