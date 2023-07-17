import re

def validate_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[$#@]", password):
        return False
    if re.search(r"\s", password):
        return False
    if re.search(r"([a-zA-Z0-9])\1\1", password):
        return False
    return True

user_password = input("Введіть пароль: ")

if not validate_password(user_password):
    print("Пароль не відповідає вимогам. Спробуйте ще раз.")
    user_password = input("Введіть пароль: ")

print("Пароль відповідає вимогам.")
