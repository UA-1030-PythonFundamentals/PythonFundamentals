C = 0.0
F = 0.0
C = float(input("Enter a temperature in Celsius \n"))

if C > -273.15:
    F = (C * 9 /5) + 32
    print(str(C)+"C","is equivalent to",str(F)+"F")
else:
    print("Invalid temterature")