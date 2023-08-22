def divide(numerator, denominator):
    try:
        result = numerator / denominator
        return  f"Result is {result}"
    except ZeroDivisionError as e:
        return f"Oops, {numerator}/{denominator}, {e} is error!!!"
    except TypeError as e:
        return f"Value Error! You did not enter a number!"