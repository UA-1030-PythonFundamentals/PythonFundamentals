def divide(numerator, denominator):
    try:
        if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
            raise ValueError
        return f'Result is {float(numerator) / float(denominator)}'
    except ValueError:
        return 'Value Error! You did not enter a number!'
    except ZeroDivisionError:
        return f'Oops, {numerator}/{denominator}, division by zero is error!!!'


print(divide(4, 8))
print(divide(4, 0))
print(divide('4', 8))
