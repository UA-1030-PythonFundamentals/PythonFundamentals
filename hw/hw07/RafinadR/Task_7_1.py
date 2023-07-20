def bigger(a, b):

    """What of two numbers is bigger: a or b"""
    0
    if a > b:
        print(f"{a} > {b}")

    elif a < b:
        print(f"{a} < {b}")

    else:
        print(f"{a} = {b}")

print(bigger.__doc__)
# bigger(6, 3)
# bigger(5, 10)
# bigger(7, 7)
bigger(int(input("a = ",)), int(input("b = ")))