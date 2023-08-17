import re

password = input("Enter your password: ")
count = 0
while True:
    if (len(password) > 16):
        count = -1
        break
    elif (len(password) < 6):
        count = -1
        break
    elif not re.search("[a-z]", password):
        count = -1
        break
    elif not re.search("[A-Z]", password):
        count = -1
        break
    elif not re.search("[0-9]", password):
        count = -1
        break
    elif not re.search("[$#@]", password):
        count = -1
        break
    elif re.search("\s", password):
        count = -1
        break
    else:
        count = 0
        print("Valid Password")
        break

if count == -1:
    print("Not a Valid Password ")

