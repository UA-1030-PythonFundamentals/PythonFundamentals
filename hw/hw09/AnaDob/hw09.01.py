import random

def play_guessing_game():
    secret_number = random.randint(1, 100)

    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print("You have 10 attempts to guess it.")

    attempts = 0

    while attempts < 10:
   
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        attempts += 1

        if user_guess == secret_number:
            print("Congratulations! You guessed the number!")
            break
        elif user_guess < secret_number:
            print("The number is greater than your guess.")
        else:
            print("The number is less than your guess.")

    else:
        print(f"Game over. The number was {secret_number}.")

if __name__ == "__main__":
    play_guessing_game()
