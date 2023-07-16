import random as rd
number = rd.randint(1,100)
print(number)
for t in range(1,11):
    print(f'Try №{t}')
    choice = int(input('Your guess: '))
    if choice==number:
        print('Congratulation! You won!')
        break
    elif choice>number:
        print('Your number is more')
    elif choice<number:
        print('Your number is less')
