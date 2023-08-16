def celsius_to_fahrenheit(temps):
    return list(map(lambda x: x*9/5+32, temps))


celsius_temperatures = [0, 10, 20, 30, 40]
print(celsius_to_fahrenheit(celsius_temperatures))