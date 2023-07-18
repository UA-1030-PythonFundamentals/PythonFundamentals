import random
counter = 0
user_name = input("Hello! What is your name? \n")
number = random.randint(1, 100)

while counter < 10:
    guess_number = int(input("Enter your number from range 1 to 100: "))
    if guess_number == number:
        print(f"Good job, {user_name}! You are the winner!")
        break
    elif 1 <= guess_number <= 100 and guess_number < number:
        print("Your number is too low! Try again \U0001f600")
    elif 1 <= guess_number <= 100 and guess_number > number:
        print("Your number is too high! Try again \U0001f600")
    else:
        print("Your number is not in the range of 1 to 100! Try again \U0001f600")
    counter += 1

if counter >= 10:
    print(f"Game over, {user_name}! You ran out of attempts. The correct number was {number}.")