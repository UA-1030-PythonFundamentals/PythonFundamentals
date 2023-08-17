def check_odd_even(number):
    try:
        number = int(number)
    except:
        return 'You entered not a number.'

    if not number % 2:
        return 'Entered number is even'
    else:
        return 'Entered number is odd'


print(check_odd_even(15))
print(check_odd_even(16))
print(check_odd_even('str'))
