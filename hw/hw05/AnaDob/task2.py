
fibonacci_numbers = int(input("What is the n number? "))

a, b = 0, 1
count = 0


if fibonacci_numbers <= 0:
   print("Please enter a positive integer")
elif fibonacci_numbers == 1:
   print("Fibonacci sequence upto",fibonacci_numbers,":")
   print(a)
else:
   print("Fibonacci numbers:")
   while count < fibonacci_numbers:
       print(a)
       c = a + b
       a = b
       b = c
       count += 1
