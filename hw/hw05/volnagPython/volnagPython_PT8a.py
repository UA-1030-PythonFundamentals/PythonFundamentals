#HW5 PT8a --Factorial of an integer
def fak_rial(n):
    '''Calculates a factorial of whole nambers'''
    if n == 0:
        print("Factorial = 1")
    else:
        fac = 1
        for i in range(1,n+1):
            fac = fac * i
        print(f"Factorial of {n} equals {fac}")
print()
    
