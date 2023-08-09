import re

requirements = ['at least 1 letter between [a-z] and 1 letter between [A-Z]',
                'at least 1 number between [0-9]',
                'at least 1 character from [$#@]',
                'minimum length 6 characters',
                'maximum length 16 characters'
                ]
print(f"Validation requirements: ")
for requirement in requirements:
    print(requirement)
def check_validity(password):
    if not 6 <= len(password) <= 16:
        print(f"Error: {requirements[4]} and {requirements[3]}")
    elif not re.search(r'[$|#|@]', password):
        print(f'Error: {requirements[2]}')
    elif not re.search(r'\d', password):
        print(f'Error: {requirements[1]}')
    elif not re.search(r'[A-Z]', password):
        print(f'Error: {requirements[0]}')
    elif not re.search(r'[a-z]', password):
        print(f'Error: {requirements[0]}')
    else:
        print('Your password is great!')
        return True

flag = False
while flag != True:
    password = input("Enter your password: ")
    flag = check_validity(password)
