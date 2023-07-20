import random


def guess_number(number):
    """Guesses a number from 1 to 100 in 10 tries."""
    attempts = 0
    while attempts < 10:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess == number:
            print("Congratulations, you guessed the number!")
            return
        elif guess < number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        attempts += 1
    print("You have used all 10 attempts.")
    print("The number was:", number)


def main():
    number = random.randint(1, 100)
    guess_number(number)


if __name__ == "__main__":
    main()
