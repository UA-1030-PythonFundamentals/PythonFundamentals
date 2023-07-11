import re


def main():
    password = input('Enter the password: ')

    if not re.search(r'[a-z]', password):
        print('Password must contain at least 1 letter between [a-z]')
    elif not re.search(r'[A-Z]', password):
        print('Password must contain at least 1 letter between [A-Z]')
    elif not re.search(r'\d', password):
        print('Password must contain at least 1 number between [0-9]')
    elif not re.search(r'[$|#|@]', password):
        print('Password must contain at least 1 charscter from [$|#|@]')
    elif len(password) < 6:
        print('Minimum lenght must be 6 symbols')
    elif len(password) > 16:
        print('Maximum lenght must be 16 symbols')
    else:
        print('Password is correct')


if __name__ == '__main__':
    main()
