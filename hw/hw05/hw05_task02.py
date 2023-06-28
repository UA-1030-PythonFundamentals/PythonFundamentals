def fibonacci_numbers(num):
    if numbers <= 0:
        print("Enter a number greater than 0")
        return

    first_num = 0
    second_num = 1

    print(first_num)
    print(second_num)

    while second_num <= num:
        next_num = first_num + second_num
        print(next_num)
        first_num = second_num
        second_num = next_num


numbers = int(input("Enter a number: "))
fibonacci_numbers(numbers)
