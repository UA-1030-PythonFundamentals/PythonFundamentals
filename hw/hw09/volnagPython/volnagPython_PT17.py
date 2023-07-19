##Task 1. Write a game script that randomly generates a number from a range of
##1 to 100 and asks the user to guess that number in 10 tries.
##The program reads the numbers entered by the user and prompts the user
##whether the guessed number is greater or less than the number entered by the
##user. The game must continue until the user has used 10 attempts and guessed
##the number. If the user guessed the number, the program prints a
##congratulatory message, and if 10 attempts have been exhausted and the user
##did not have time to guess the number, then the corresponding message is
##displayed.
##(to perform the task, you need to import the random module,
##and from it the randint() function) -- HW09---July 14,2023

import random

num_rand = random.randint(1,100)

i = 0
while i < 10:
    num = int(input("\nEnter a number between 1 and 100 : = \n"))
    if num == num_rand:
      print()
      print("----- Congrats! Your guess is right! -----")
      break
    elif num <= num_rand:
      print("This number is LESS then the target one.")
    elif num >= num_rand:
      print("This number is GREATER then the target number.")
    i += 1
  #print(f"{i}th trial")
else:
    print()
    print("------ You are out of trials! ------")

#VN
