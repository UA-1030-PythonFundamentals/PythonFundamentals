##Write a program that alyzes the entered number and, depending on the number, gives
##the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). Take
##into account cases of entering numbers from 8 and more,
#as well as cases of entering nonnumerical data. --HW11--PT23-- Aug 3, 2023

from weekdays import num 

print(70*"*")
den = input ("Enter the integer corresponding to the day of week number :\n")

dat = num(den)

match dat:
    case 1:
        print ("--Monday--")
    case 2:
        print ("--Tuesday--")
    case 3:
        print ("--Wednesday--")
    case 4:
        print ("--Thursday--")
    case 5:
        print ("--Friday--")
    case 6:
        print ("--Saturday--")
    case 7:
        print ("--Sunday--")
    case _:
        print("Something's wrong with the integer you've entered...")

print(70*"*")

#VN
