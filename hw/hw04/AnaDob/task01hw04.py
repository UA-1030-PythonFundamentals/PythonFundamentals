celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius * 9/5 + 32
if celsius < -273.15:
    print ("Temperature is below absolute zero (-273.15 C)")
else:
    print("The %0.f C is equivalent to %0.1f F" %(celsius,fahrenheit))

        
   
