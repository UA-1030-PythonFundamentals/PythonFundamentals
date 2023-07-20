print("Password requirements:\n \
    At least 1 letter between [a-z] and 1 letter between [A-Z].\n \
    At least 1 number between [0-9].\n \
    At least 1 character from [$#@].\n \
    Minimum length 6 characters.\n \
    Maximum length 16 characters")
pas = input("Create your password:\n")
count = 1


while count < 5:
    if any(i.islower() for i in pas) \
            and any(i.isupper() for i in pas) \
            and any(i.isdecimal() for i in pas) \
            and 6 <= len(pas) <= 16 \
            and any(i == "$" or i =="#" or i =="@" for i in pas):
    
        print("Save your password:", pas)
        break
    
    else:
        print("Your password does not meet the requirements, try again")
        pas = input("Enter your password:\n")
        count +=1
if count == 5:
    print("Try again later, use password requirements")