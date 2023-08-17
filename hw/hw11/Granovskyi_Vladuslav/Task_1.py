class Error(Exception):
    def __init__(self, info):
        self.info = info

    def __str__(self):
        return self.info

def info_age():
    age = int(input("Введіть ваш вік:"))

    if age < 0:
        raise Error("Error")
    else:
        if age % 2 == 0:
            return 'Ваш вік парний'
    return 'Ваш вік непарний'

print(info_age())