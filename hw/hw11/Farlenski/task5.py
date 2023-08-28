def check_odd_even(number):
    try:
        if not number%2:
            return "Entered number is even"
        else:
            return "Entered number is odd"
    except TypeError:
        return "You entered not a number."