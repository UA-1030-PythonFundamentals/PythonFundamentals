def sum(a,b):
    return a+b*10

def largest(arg1, arg2):
    """This function returns the largest numbers of two numbers"""
    answer = ""
    if arg1 == arg2:
        answer = "Two number are equal"
    elif arg1 > arg2 > 15:
        answer = sum(arg1, arg2)
        if answer > 1000:
            answer = "foo"
    else:
        answer = f"The largest number is {max(arg1, arg2)}"

    return answer