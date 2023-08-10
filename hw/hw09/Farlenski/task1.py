from random import randint

number = randint(1, 100)
counter = 0

while counter != 10:
    guess_number = int(input("Enter your number from range: 1 to 100:"))

    if guess_number == number:
        print(f"Good job! You're winner!")
        break
    elif 1 <= guess_number <= 100 and guess_number < number:
        print("Your number is less!")
    elif 1 <= guess_number <= 100 and guess_number > number:
        print("Your number is more!")
    else:
        print("Your number is not in range 1 to 100!")

    counter += 1

    if counter == 10:
        print("You lost! Better luck next time!")