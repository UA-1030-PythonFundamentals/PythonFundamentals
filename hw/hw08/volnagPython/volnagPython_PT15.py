##Task2.
##Write pwd Python program to check the validity of a password (input from users).
##Validation :
##At least 1 letter between [a-z] and 1 letter between [A-Z].
##At least 1 number between [0-9].
##At least 1 character from [$#@].
##Minimum length 6 characters.
##Maximum length 16 characters. -- HW08 PT14 --- July 11,2023
print(70*"*")
          # Regular Expression matching operations 
import re


pwd = input ("Enter your password : \n")

dim1 = len(pwd)
min_dim = 6
max_dim = 16

res5 = re.findall("[pwd-z]",pwd)    #returns a list
res6 = re.findall("[A-Z]",pwd)      #returns a list
res7 = re.findall("[0-9]",pwd)      #returns a list
res8 = re.findall("[$#@&_=]",pwd)   #returns a list

dim5 = len(res5) 
dim6 = len(res6)
dim7 = len(res7)
dim8 = len(res8)
                #Checking validity
if dim5 and dim6 and dim7 and dim8 and dim1 > min_dim and dim1 <= max_dim:
    print("Password is valid!")
else:
    print("Your password is not valid! Try another one.")
print(70*"*")
#VN
