# Fibonacci sequence
def main():
    stop_number = int(input('Enter stop number: '))
    if not stop_number:
        print(f'Fibonacci numbers up to {stop_number}: 0')
        return

    fibo_numbers = [0, 1]

    while fibo_numbers[-1] + fibo_numbers[-2] < stop_number:
        fibo_numbers.append(fibo_numbers[-1] + fibo_numbers[-2])

    print(f'Fibonacci numbers up to {stop_number}:', end=' ')
    print(*fibo_numbers, sep=', ')


if __name__ == '__main__':
    main()