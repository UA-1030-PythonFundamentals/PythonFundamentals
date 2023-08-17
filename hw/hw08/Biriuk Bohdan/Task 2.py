import re

def g_pass():
    password = input("Create your password: ")


    if len(password) > 16:
        print("Password long")
    elif len(password) < 6:
        print("Password short")
    elif not re.findall(r"[a-z]", password):
        print("The password must contain: a-z")
    elif not re.findall(r"[A-Z]", password):
        print("The password must contain: A-Z")
    elif not re.findall(r"[0-9]", password):
        print("The password must contain: 0-9")
    elif not re.findall(r"[$#@]", password):
        print("The password must contain: $#@")
    else:
        print("Your password correct")

test = print(g_pass())