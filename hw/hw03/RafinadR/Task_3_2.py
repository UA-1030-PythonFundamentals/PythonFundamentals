number = input("Enter a four-digit natural number:\n")
l = len(number)
if l == 4 and number.isdecimal():
   
    a = int(number[0])
    b = int(number[1])
    c = int(number[2])
    d = int(number[3])
    n1 = (a * b * c * d)
    
    print("Product of the digits:", n1)
    print ("Revers: ", int(number[::-1]))
    print("Sorted: ", sorted(number))

else:
    print("Your number in not four-digits natural number")