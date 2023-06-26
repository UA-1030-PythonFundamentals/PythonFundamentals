import random

print("Task 1")
print()
print("Hello world \U0001F600 ")
print()
print("Task 2")

name = str(input("Hello! What is your name? "))
number = random.randint(1, 40)

print(f'Well, {name}, I am thinking of a number between 1 and 40.')

count = 0
while count < 10:
    try:
        guess_number = int(input('Take a guess! Enter your number: '))
    except ValueError:
        print("Некорректный ввод. Попробуйте еще раз.")
        continue

    if guess_number == number:
        print(f'Good job, {name}! You are a winner!')
        break

    elif 1 <= guess_number <= 40 and guess_number < number:
        count += 1
        print('Your number is less.')

    elif 1 <= guess_number <= 40 and guess_number > number:
        count += 1
        print('Your number is more.')

    elif not 1 <= guess_number <= 40:
        count += 1
        print("Your number is not in the range 1 to 40. Try again :)")
