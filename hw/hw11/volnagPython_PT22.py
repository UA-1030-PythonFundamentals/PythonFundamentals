##2. Write a program that prompts the user to enter their age, and then displays a
##message stating whether the age is even or odd. The program must provide the ability
##to enter a negative number, and in this case generate an exception. The master code
##should call a function that processes the information entered. --HW11--PT22--Aug.1, 2023

from age import num


age = input("Enter a number of years corresponding to your age :\n")

dat = num(age)

if dat is None:
    pass
else:
    if dat % 2 == 0:
        print("You have lived the even number of years.")
    else:
        print("You have lived the odd number of years.")

    print(70*"*")
    print(f"---You are {dat} years old!---")

#VN
