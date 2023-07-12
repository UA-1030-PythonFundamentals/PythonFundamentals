def largest_number(a, b):
    """Takes in two numbers, returns largest one."""
    if a > b:
        return a
    else:
        return b

print(largest_number.__doc__)
print(largest_number(789,8))