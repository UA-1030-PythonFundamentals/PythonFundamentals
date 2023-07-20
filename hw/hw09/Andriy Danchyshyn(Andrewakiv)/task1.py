import random

number = random.randint(1, 100)

counter = 0

print('Guess a number between 1 and 100: ')

while counter < 10:

    guess_number = int(input('Enter your number: '))

    if guess_number == number:
        print('You are a winner!')
        break

    elif 1 <= guess_number <= 100 and guess_number < number:
        print('Your number is less.')
        counter += 1

    elif 1 <= guess_number <= 100 and guess_number > number:
        print('Your number is more.')
        counter += 1

    elif not 1 <= guess_number <= 100:
        print(f"Your number is not in the range 1 to 40. Try again:)")
        counter += 1
