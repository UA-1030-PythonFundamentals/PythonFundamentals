# It's HW4 PT1 , June 23,2023
print('Hello!')
print(70*"*")

    # Temperature value input
t = float(input('Please, enter your temperature : \n'))
print()
   
    # Specifying the units for temperature
unitz = input('Is it in degrees Celcius (C) or in degrees Farenheit (F)?\n')
cls=["C","c"]
frg=["F","f"]
print()
    #Conversion of degrees
if t >= -273.15 and unitz in cls:
    funitz = t*9/5 + 32
    funitz = round(funitz,1)
    print('Temperature of ' + str(t) + ''+ u'\N{DEGREE SIGN}C '+\
         ' is equal to '+str(funitz)+''+ u'\N{DEGREE SIGN}F')

elif t >= -459.7 and unitz in frg:
    cunitz=5/9*(t-32)
    cunitz=round(cunitz,1)
    print('Temperature of ' + str(t) + '' + u'\N{DEGREE SIGN}F' +\
          ' is equal to ' + str(cunitz) + '' + u'\N{DEGREE SIGN}C')

elif unitz not in cls and unitz not in frg:
    print('Wrong units. Try again!')

else:
    print("Error: Entered temperature is below absolute zero"+ \
          "(-273.15"+u'\N{DEGREE SIGN}C'+" or "+\
          "-459.7"+u'\N{DEGREE SIGN}F'+")"+")! ")

print(70*"*")
#VN
