def celsius_to_fahrenheit(temps):
    return [x*9/5+32 for x in temps]


celsius_temperatures = [0, 10, 20, 30, 40]
print(celsius_to_fahrenheit(celsius_temperatures))