def largest(arg1, arg2):
    """This function returns the largest numbers of two numbers"""
    answer = ""
    if arg1 == arg2:
        answer = "Two number are equal"
    else:
        answer = f"The largest number is {max(arg1, arg2)}"

    return answer


print(largest.__doc__)
#print(largest(12, 12))
print(largest(21, 12))