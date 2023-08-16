from random import randint

num = randint(1, 100)
counter = 0

while counter != 10:
    number = int(input("Write your number:"))

    if number == num:
        print("You WIN!")
        break
    elif 1 <= number <= 100 and number < num:
        print("Your number is less!")
    elif 1 <= number <= 100 and number > num:
        print("Your number is more!")
    elif not 1 <= number <= 100:
        print("Your number is not in the range 1-100")

    counter += 1

    if counter == 10:
        print("you LOSE!")
