class MyError(Exception):
    def __init__(self, message):
        super().__init__(message)


def check_positive(number):
    try:
        number = float(number)

        if number > 0:
            return f"You input positive number: {number}"
        elif number < 0:
            raise MyError(f"You input negative number: {number}. Try again.")
        else:
            raise ValueError
    except MyError as e:
        return e
    except ValueError:
        return "Error type: ValueError!"


print(check_positive(5))
print(check_positive(-10))
print(check_positive(0))
print(check_positive("abc"))
