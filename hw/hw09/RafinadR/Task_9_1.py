import random

t_number = random.randint(1, 100)

count = 0

print("Gues number! You have 10 attempts from 1 to 100")

while count < 10:

    number = input("Enter your number:\n")

    if number.isdecimal():
        number = (int(number))

        if number < t_number and 1 <= number <= 100:
            print("Your number is less")
            count += 1
        if number > t_number and 1 <= number <= 100:
            print("Your number is greater")
        if number == t_number:
            print(f"Great, your number {number} is correct! You guessed it and you WIN АВТОМОБІЛЬ!!!")
            break
        if number < 1 or number > 100:
            print("Your number is not 1-100")
            count += 1
        if count == 10:
            print("Sorry, 10 attempts are over. You lost :( ")
            break
    else:
        print("You enter not integer number from 1 to 100")
        count += 1
        if count == 10:
            print("Sorry, 10 attempts are over. You lost :( ")