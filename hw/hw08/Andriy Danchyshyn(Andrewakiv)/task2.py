import re


def is_valid():
    password = input('Enter your password: ')
    res = re.findall(r'[a-z]+|[A-Z]+|[0-9]+|[#@$]+', password)
    if 6 <= len(password) <= 16 and len(res) == 4:
        return True
    return False


print(is_valid())
