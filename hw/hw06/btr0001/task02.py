attempts = 5

while attempts > 0:
    name = input('Enter your name: ')
    if name == 'First':
        print(f'Welcome {name}!')
        break
    else:
        print('Wrong name')
        attempts -= 1

