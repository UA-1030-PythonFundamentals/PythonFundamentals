# Factorial
def main():
    stop_number = int(input('Enter stop number: '))
    factorial = 1
    for number in range(1, stop_number + 1):
        factorial *= number

    print(f'The factorial of {stop_number} equals', factorial)


if __name__ == '__main__':
    main()