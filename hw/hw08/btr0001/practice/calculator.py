from tools import *

op = input('Select operation (a, s, m, d): ')
if op not in ['a', 's', 'm', 'd']:
    print('Operation not recognized')
else:
    a = float(input('Input a: '))
    b = float(input('Input b: '))
    match op:
        case 'a':
            print(f'Result of adding {add(a, b)}')
        case 's':
            print(f'Result of subtracting {subtract(a, b)}')
        case 'm':
            print(f'Result of multiplying {multiply(a, b)}')
        case 'd':
            print(f'Result of dividing {divide(a, b)}')
