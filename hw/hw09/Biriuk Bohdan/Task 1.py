from random import randint

count = 0
number = randint(1, 100)
print("Hello, this is a guess the number game. You have 10 attempts, good luck")

while True:
    guess = int(input("Enter your number: "))
    count += 1
    if guess > number:
        print("Number is less")
    if guess < number:
        print("Number is greater")
    if count == 10:
        print("You loose, my number is: {0}".format(number))
        break
    if guess == number:
        break

if guess == number:
    print("Congratulations, you WON !!!")