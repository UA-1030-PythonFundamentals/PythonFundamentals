from random import randint

counter = 10

number = randint(0, 100)

while counter > 0:
    counter -= 1
    n = int(input('Input number: '))
    if number > n:
        print('Guessed number is grater')
    elif number < n:
        print('Guessed number is less')
    else:
        print('Congratulations, you won!')
        break
else:
    print('You loose')
