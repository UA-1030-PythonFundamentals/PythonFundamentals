import re

def valid_password():
    user_password = input('Enter your password: ')
    res = re.findall(r'[a-z]+|[A-Z]+|[0-9]+|[#@$]+', user_password)

    if 6 <= len(user_password) <= 16 and len(res) == 4:
        return "Good password"
    return "Bad password"


print(valid_password())
