class MyError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data


def check_age():
    age = int(input('Enter your age: '))

    if age < 0:
        raise MyError('Enter a positive number')
    else:
        if age % 2 == 0:
            return 'age is even'
    return 'age is odd'


print(check_age())
