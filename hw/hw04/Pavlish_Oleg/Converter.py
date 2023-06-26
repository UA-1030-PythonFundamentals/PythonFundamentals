first_temp = float(input('Temperature (Celsius): \n- '))
if first_temp<=(-273.15):
    print('ERROR: TEMPERATURE BELOW ABSOLUTE ZERO')
else:
    print(first_temp*(9/5)+32, 'F')