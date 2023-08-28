class MyError(Exception):
    pass


def check_positive(number):
    try:
        number = float(number)
    except (TypeError, ValueError):
        return MyError("Error type: ValueError!")
    if number >= 0:
        return f"You input positive number: {number}"
    else:
        return MyError(f"You input negative number: {number}. Try again.")