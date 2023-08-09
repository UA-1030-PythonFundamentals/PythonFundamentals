def find_largest_number(num1, num2):
    """
    Returns the largest number among two input numbers.

    Parameters:
        num1 (int or float): The first number.
        num2 (int or float): The second number.

    Returns:
        int or float: The largest number between num1 and num2.
    """
    return max(num1, num2)
result = find_largest_number(5, 10)
print(result)  