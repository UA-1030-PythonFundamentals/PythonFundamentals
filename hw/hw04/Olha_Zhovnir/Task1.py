Celsius = float(input('Enter the temperature in Celsius:\n'))
def temperature_converter(Celsius):
    if Celsius > -273.15:
        Fahrenheit_temp = round(Celsius*(9/5)+32, 2)
        print(f'{Celsius} C is equivalent to {Fahrenheit_temp} F')
    else:
        print("The temperature is below absolute zero(-273.15 C)")

temperature_converter(Celsius)
